from datetime import datetime, timedelta


from airflow_scd.dags.logger import logger_db

from system.db.factory import DBFactory
from system.celery import celery_app

# connections
DB_MANAGER = DBFactory.create()()
DB_MANAGER._create_connection()

# constants
BATCH_LIMIT = 100  # database read batch limit


#mycareersfuture
def transform_job_location(job_location):
    job_location_list = []
    for indx in range(len(job_location["districts"])):
        district_location = job_location["districts"][indx]["location"] if job_location["districts"][indx]["location"] != None else " "
        region_location = job_location["districts"][indx]["region"] if job_location["districts"][indx]["region"] != None else " "
        job_location_list.append(district_location+" "+region_location)
    return job_location_list


@celery_app.task(name="manipulate_mycareersfuture_location", ignore_result=False,
                 acks_late=True, queue="maintenance", expires=60 * 60 * 3)
def manipulate_mycareersfuture_location():
    logger_db._info_mixin(f"Finding 100 data From The db")
    DB_MANAGER.set_collection("jds", "mycareersfuture")
    FIND_CONDITION = {
        "updated_at": {"$lt": datetime.now() - timedelta(days=7)},
        "job_location_list": {
            "$exists": False
        }
    }
    db_docs = DB_MANAGER._find(FIND_CONDITION).limit(BATCH_LIMIT)
    logger_db._info_mixin(f"find successful")

    for elem in db_docs:

        doc_id = elem['_id']
        logger_db._info_mixin(f"processing object id {doc_id}")
        transformed_job_location = transform_job_location(elem['job_location'])
        filter = {"_id": doc_id}
        update = {
            "job_location": "Multiple location",
            "job_location_list": transformed_job_location,
            "updated_at": datetime.now()
        }
        DB_MANAGER._update_one(filter, update)


if __name__ == '__main__':
    manipulate_mycareersfuture_location()




with DAG(default_args=default_args, dag_id='mycareersfuture_dag', **mycareersfuture_joblocation_config) as mycareersfuture_dag:
    mycareersfuture = PythonOperator(task_id='mycareersfuture_dag',
                                    python_callable=manipulate_mycareersfuture_location_job,
                                    dag=mycareersfuture_dag)


def manipulate_mycareersfuture_location_job():
    from maintenance.mycareersfuture import manipulate_mycareersfuture_location
    manipulate_mycareersfuture_location.apply_async(queue='maintenance', serializer="json")

mycareersfuture_joblocation_config = {
    "schedule_interval": "* * * * *",
    "start_date": days_ago(1),
    "catchup": False,
    "concurrency": 1,
    "max_active_runs": 1,
    "dagrun_timeout": 7200
}