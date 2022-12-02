# getting tasks where duplicate records exists and note those collections/tasks
from test2 import report

from pymongo import MongoClient
import ssl

uri1 = ""
mongo_conn = MongoClient(uri1, connect=False, ssl_cert_reqs=ssl.CERT_NONE)


def check_duplication(db_name, coll_name, unique_key):
    source_coll = mongo_conn[db_name][coll_name]
    unique_key = "$"+unique_key
    try:
        docs = list(source_coll.aggregate([
            {"$group": {"_id": unique_key, "count": {"$sum": 1}}},
            {"$match": {"_id": {"$ne": None}, "count": {"$gt": 1}}}
        ]))
    except Exception as e:
        print(e)
        return
    if docs:
        return True
    else:
        return False


def get_duplicate_records_collection_names(conn, task_names):
    duplicate_collection_names = []
    for task in task_names:
        doc = list(conn.find({"task": task}))
        unique_key = doc[0]["producer"]["unique_key"]
        db_name = doc[0]["producer"]["collections"]["output_collection"].split(".")[0]
        coll_name = doc[0]["producer"]["collections"]["output_collection"].split(".")[1]
        if check_duplication(db_name, coll_name, unique_key):
            duplicate_collection_names.append((task, coll_name))
    return duplicate_collection_names


def get_task_name(conn):
    duplicate_rec_task = dict()
    for k, v in report.items():
        duplicate_collection_names = get_duplicate_records_collection_names(conn, v)
        duplicate_rec_task[k] = duplicate_collection_names
    return duplicate_rec_task


if __name__ == "__main__":
    conn = mongo_conn['workflow']['harvester_config']
    duplicate_rec_report = get_task_name(conn)
    for k, v in duplicate_rec_report.items():
        print(k, v)
