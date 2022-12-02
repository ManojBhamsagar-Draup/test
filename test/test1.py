# getting task names according to harvests types where unique key is not detail url

from pymongo import MongoClient
import ssl

uri1 = ""

mongo_conn = MongoClient(uri1, connect=False, ssl_cert_reqs=ssl.CERT_NONE)


def get_tasks(conn):
    docs = list(conn.find({"producer.unique_key": {"$exists": True}}))
    return docs


def filter_tasks_by_unique_key(tasks):
    new_tasks = []
    for task in tasks:
        if task["producer"]["unique_key"] != "detail_url":
            new_tasks.append(task)
    return new_tasks


def remove_metadata_processes(tasks):
    new_tasks = []
    for task in tasks:
        if task["producer"]["collections"]["output_collection"].split(".")[0] != "metadata":
            new_tasks.append(task)
    return new_tasks


def filter_tasks_by_harvest_type(tasks):
    report = dict()
    for task in tasks:
        harvest_type = task["producer"]["collections"]["output_collection"].split(".")[0]
        if harvest_type in report:
            report[harvest_type].append(task["task"])
        else:
            report[harvest_type] = [task["task"]]
    return tasks, report


if __name__ == "__main__":
    conn = mongo_conn['workflow']['harvester_config']
    tasks = get_tasks(conn)
    tasks = filter_tasks_by_unique_key(tasks)
    tasks = remove_metadata_processes(tasks)
    tasks, report = filter_tasks_by_harvest_type(tasks)
    for k, v in report.items():
        print(v)
