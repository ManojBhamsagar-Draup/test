from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from utils.db_ops import connect_to_coll


def move_to_ten_times():
    SOURCE_DB_NAME = "schema_validated_errors"
    SOURCE_COLL_NAME = "ten_times_events_details"
    DEST_DB_NAME = "events"
    DEST_COLL_NAME = "ten_times"

    coll1 = connect_to_coll(db_name=SOURCE_DB_NAME, collection_name=SOURCE_COLL_NAME)
    coll2 = connect_to_coll(db_name=DEST_DB_NAME, collection_name=DEST_COLL_NAME)

    FIND_CONDITION = {
            "details.organiser": {
                "$ne": None
            },
            "details.event_name": {
                "$ne": None
            }
        }

    doc_list = list(coll1.find(FIND_CONDITION))

    URL_FIELD = "detail_url"

    for ele in doc_list:
        coll2.update_one(
            {
                "detail_url": ele[URL_FIELD]
            },
            {
                "$set": {
                    "details": ele.get("details"),
                    "visitors_flag": ele.get("visitors_flag", False),
                    "speakers_flag": ele.get("speakers_flag", False),
                    "exhibitors_flag": ele.get("exhibitors_flag", False),
                    "updated_at": datetime.now()
                }
            }
        )
    coll1.close()
    coll2.close()

def create_airflow_dags():
    move_ten_times_config = {
        "schedule_interval": "0 10 * * *",
        "start_date": days_ago(1),
        "catchup": False,
        "concurrency": 1,
        "max_active_runs": 1,
        "dagrun_timeout": 3600
    }
    default_args = {
        'email': ['harvestor@draup.com'],
        'email_on_failure': True,
        'retries': 0
    }
    globals()["ten_times_migrate"] = DAG(default_args=default_args, dag_id='ten_times_migrate',
                                         **move_ten_times_config)
    ten_times = PythonOperator(task_id='ten_times_migrate', python_callable=move_to_ten_times,
                                  dag=globals()["ten_times_migrate"])


create_airflow_dags()
