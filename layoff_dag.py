from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from utils.db_ops import connect_to_coll
import pandas as pd


def get_employee_details():
    SOURCE_DB_NAME = "harvests"
    SOURCE_COLL_NAME = "layoff_details"

    coll1 = connect_to_coll(db_name=SOURCE_DB_NAME, collection_name=SOURCE_COLL_NAME)

    FIND_CONDITION = {"link": {"$exists": True}}

    doc_list = list(coll1.find(FIND_CONDITION))

    for ele in doc_list:
        sheet_url = ele.get("harvesting_link", "")
        try:
            url = sheet_url + "/export?format=csv"
        except Exception as e:
            print(repr(e))
            continue
        try:
            df = pd.read_csv(url)
            flag = False
            no_cols = False
            sample_colnames = ["linkedin", "location"]
            count = df.shape[0]
            while count > 1:
                cols = list(df.columns)
                for col in cols:
                    try:
                        col = col.lower()
                    except Exception as e:
                        print(repr(e))
                        print(f"cannot convert {col} to lower")
                        continue
                    if any(sample_colname in col for sample_colname in sample_colnames):
                        flag = True
                        if "linkedin.com" in col:
                            no_cols = True
                        break
                if not flag:
                    new_header = df.iloc[0]
                    df = df[1:]
                    df.columns = new_header
                else:
                    break

            if flag and no_cols:
                generated_column_names = []
                for i in range(df.shape[1]):
                    generated_column_names.append('column'+str(i))
                df.columns = generated_column_names

            df = df.dropna(axis=1, how='all')
            df.reset_index(inplace=True, drop=True)
            employee_list = []
            for index, rows in df.iterrows():
                employee_list.append(df.iloc[index].to_dict())
                coll1.update_one(
                    {
                        "id": ele["id"]
                    },
                    {
                        "$set": {
                            "employees_details": employee_list,
                        }
                    },
                    upsert=True
                    )
        except Exception as e:
            print(repr(e))
            print(f"couldn't get employee data from sheet url: {sheet_url}")


def create_airflow_dags():
    employee_details_config = {
        "schedule_interval": "0 5 * * *",
        "start_date": days_ago(1),
        "catchup": False,
        "concurrency": 1,
        "max_active_runs": 1,
        "dagrun_timeout": 1200
    }
    default_args = {
        'email': ['harvestor@draup.com'],
        'email_on_failure': True,
        'retries': 0
    }
    globals()["layoff_details"] = DAG(default_args=default_args, dag_id='layoff_details',
                                         **employee_details_config)
    ten_times = PythonOperator(task_id='layoff_details', python_callable=get_employee_details,
                                  dag=globals()["layoff_details"])


create_airflow_dags()
