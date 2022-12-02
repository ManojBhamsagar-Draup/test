from utils.gateway.data_fetch import get_data_gateway_api
from system.logger.factory import LoggerFactory
from system.celery import celery_app
import json
import tldextract
from utils.db_ops import bulk_upsert_with_doc_update

logger = LoggerFactory.create(name="SimilarSites")
logger_context = "SimilarSitesMetaProcess"

ECOSYSTEM_COMPANIES_URL = "https://gateway.draup.technology/api/iris1/v1.0/iris1_templates_data?template=Ecosystem%20Company%20Schema&page={0}&pagesize=100"
CONSUL_COMPANIES_URL = "https://gateway.draup.technology/api/iris1/v1.0/etl_company_data/?page_number={0}&page_size=100"


def get_ecosystem_filtered_data(data):
    """
        filter data to get only required fields
    """
    if not data:
        return []
    filtered_data = []
    for doc in data:
        domain = doc.get("website_url", "")
        website_url = "https://www." + domain
        if domain:
            filtered_data.append({"domain": domain, "website_url": website_url})
    return filtered_data


def extract_domain_from_url(website_url):
    """
        extract domain name from website url
    """
    ext = tldextract.extract(website_url)
    domain = ext.domain + "." + ext.suffix
    return domain


def get_consul_filtered_data(data):
    """
        filter data to get only required fields
    """
    if not data:
        return
    filtered_data = []
    for doc in data:
        try:
            website_url = doc.get("domain_url", "")
            domain = extract_domain_from_url(website_url)
            if domain:
                filtered_data.append({"domain": domain, "website_url": website_url})
        except Exception as e:
            logger._exception_mixin(msg=f"couldn't get domain name due to: {repr(e)}", context=logger_context)
    return filtered_data


def updated_similar_sites_meta(data):
    """
        save data to database
    """
    if not data:
        logger._info_mixin(msg="No data to insert for this page !!", context=logger_context)
        return
    bulk_upsert_with_doc_update(
        store_db="metadata",
        store_coll="consul_similarsites_company_meta",
        job_name=logger_context,
        data=data,
        upsert_map={"domain"},
        bulk_upsert_size=100
    )


def get_ecosystem_companies():
    apply_filter = {"AND": [{"attribute": "start_up", "condition": "equal", "value": True},
                       {"attribute": "is_deleted", "condition": "equal", "value": "0"}]}
    payload = json.dumps(apply_filter)
    page = 1
    url = ECOSYSTEM_COMPANIES_URL.format(page)
    res = get_data_gateway_api(url, logger, job_context=logger_context, http_method="POST", payload=payload)
    resp = res.json()
    total_pages = resp.get("total_pages", 0)

    while page <= total_pages:
        data = resp.get("results", [])
        filtered_data = get_ecosystem_filtered_data(data)
        updated_similar_sites_meta(filtered_data)
        page += 1
        url = ECOSYSTEM_COMPANIES_URL.format(page)
        res = get_data_gateway_api(url, logger, job_context=logger_context, http_method="POST", payload=payload)
        resp = res.json()


def get_consul_companies():
    page = 1
    url = CONSUL_COMPANIES_URL.format(page)
    res = get_data_gateway_api(url, logger, job_context=logger_context)
    resp = res.json()
    total_pages = resp.get("total_pages", 0)

    while page <= total_pages:
        data = resp.get("results", [])
        filtered_data = get_consul_filtered_data(data)
        updated_similar_sites_meta(filtered_data)
        page += 1
        url = CONSUL_COMPANIES_URL.format(page)
        res = get_data_gateway_api(url, logger, job_context=logger_context)
        resp = res.json()


@celery_app.task(name="similarsites_meta_process", ignore_result=False,
                 acks_late=True, queue="maintenance", expires=60 * 60 * 8)
def similarsites_meta_process():
    get_ecosystem_companies()
    get_consul_companies()


if __name__ == "__main__":
    get_consul_companies()

# modify utils/gateway/data_fetch.py

similarsites_metadata_config = {
    "start_date": days_ago(1),
    "schedule_interval": "0 0 */15 * *",
    "catchup": False,
    'concurrency': 1,
    'max_active_runs': 1,
    'dagrun_timeout': 7200
}

def similarsites_metadata_job():
    from maintenance.similarsites_metadata import similarsites_meta_process
    similarsites_meta_process.apply_async(queue='maintenance', serializer="json")

with DAG(default_args=default_args, dag_id='similarsites_metadata',
         **similarsites_metadata_config) as similarsites_dag:
    similarsites_data = PythonOperator(task_id='similarsites_metadata',
                                  python_callable=similarsites_metadata_job,
                                  dag=similarsites_dag)