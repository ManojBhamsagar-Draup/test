from system.logger.factory import LoggerFactory
from system.celery import celery_app
from pymongo import MongoClient
import ssl
from settings.main import config

logger = LoggerFactory.create(name='IndexManager')
MONGO_URI = config.MONGO_URI

SOURCE_DB_NAME = "__mandatory_replace_with_db_name__"
SOURCE_COLL_NAME = "__mandatory_replace_with_source_collection__"
KEY_NAME = "__mandatory_replace_with_collection_name__"
CREATE_INDEX = "__optional_default_will_be_true__"
SORTING_ORDER = "__optional_default_will_be_1__"
UNIQUE = "__optional_default_will_be_False__"

index_manager_default_params = {
    "source_db_name": SOURCE_DB_NAME,
    "source_collection": SOURCE_COLL_NAME,
    "source_key_name": KEY_NAME,
    "create_index": CREATE_INDEX,
    "sorting_order": SORTING_ORDER,
    "unique": UNIQUE
}

logger_context = "IndexManager"


def validate_airflow_input(dag_run_conf):
    """
        Check if the dag is triggered with config, and has valid inputs
    """
    if not dag_run_conf:
        raise ValueError("Configuration not provided")
    source_db = dag_run_conf.get('source_db_name', '')
    source_coll = dag_run_conf.get('source_collection', '')
    key_name = dag_run_conf.get('source_key_name', '')
    if not source_db or source_db == SOURCE_DB_NAME:
        raise ValueError("Source database name is not provided")
    if not source_coll or source_coll == SOURCE_COLL_NAME:
        raise ValueError("Source collection is not provided")
    if not key_name or key_name == KEY_NAME:
        raise ValueError("key name to create index is not provided")


def check_index_existence(conn, search_key, sorting_order):
    indexes = conn.index_information()
    for index_item_key, index_item_val in indexes.items():
        if index_item_val['key'][0][0] == search_key and index_item_val['key'][0][1] == sorting_order:
            return True
    return False


def create_indexes(conn, given_key, sorting_order, unique):
    conn.create_index([(given_key, sorting_order)], background=True, unique=unique)


def remove_indexes(conn, given_key, sorting_order):
    conn.drop_index([(given_key, sorting_order)])


@celery_app.task(name="manage_indexes", ignore_result=False,
                 acks_late=True, queue="maintenance", expires=60 * 60 * 3)
def manage_indexes(**dag_run_conf):
    """
        takes parameters from airflow dag config and
        creates indexes on the specified collection.
    """
    try:
        logger._info_mixin(msg=f"Dag Run Config: {dag_run_conf} ", context=logger_context)
        validate_airflow_input(dag_run_conf)
        source_db = dag_run_conf.get('source_db_name', '')
        source_coll = dag_run_conf.get('source_collection', '')
        key_name = dag_run_conf.get('source_key_name', '')
        create_index = dag_run_conf.get('create_index', True)
        sorting_order = dag_run_conf.get('sorting_order', 1)
        unique = dag_run_conf.get('unique', False)
        mongo_conn = MongoClient(MONGO_URI, connect=False, ssl_cert_reqs=ssl.CERT_NONE)
        conn = mongo_conn[source_db][source_coll]
        if not check_index_existence(conn, key_name, sorting_order) and create_index:
            create_indexes(mongo_conn, key_name, sorting_order, unique)
            logger._info_mixin(msg=f"successfully created indexes with key {key_name} on collection {source_coll}", context=logger_context)
        if not create_index and check_index_existence(conn, key_name, sorting_order):
            remove_indexes(mongo_conn, key_name, sorting_order)
            logger._info_mixin(msg=f"successfully removed {key_name} indexes on {source_coll}", context=logger_context)
    except Exception as e:
        logger._exception_mixin(msg=f"Creation of index failed dur to: {repr(e)}", context=logger_context)




index_manager_config = {
    "start_date": days_ago(1),
    "schedule_interval": None,
    "catchup": False,
    'concurrency': 1,
    'max_active_runs': 1,
    'dagrun_timeout': 1800
}

def index_manager_job(source_db_name, source_collection, source_key_name, create_index, sorting_order, unique):
    job_kwargs = {
        "source_db_name": source_db_name,
        "source_collection": source_collection,
        "source_key_name": source_key_name,
        "create_index": create_index,
        "sorting_order": sorting_order,
        "unique": unique
    }
    from maintenance import manage_indexes
    manage_indexes.apply_async(kwargs=job_kwargs, queue="maintenance", serializer="json")

with DAG(default_args=default_args, dag_id='index_manager', **index_manager_config,
         params=index_manager_default_params) as index_manager_dag:
    manage_index = PythonOperator(task_id='index_manager', provide_context=True, python_callable=index_manager_job,
                            op_kwargs={
                                   "source_db_name": "{{ dag_run.conf['source_db_name'] }}",
                                   "source_collection": "{{ dag_run.conf['source_collection'] }}",
                                   "source_key_name": "{{ dag_run.conf['source_key_name'] }}",
                                   "create_index": "{{ dag_run.conf['create_index'] }}",
                                   "sorting_order": "{{ dag_run.conf['sorting_order'] }}",
                                   "unique": "{{ dag_run.conf['unique'] }}"
                               },
                               dag=index_manager_dag)