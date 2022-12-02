from test2 import report

from pymongo import MongoClient, DESCENDING
import ssl

uri = ""
mongo_conn = MongoClient(uri, connect=False, ssl_cert_reqs=ssl.CERT_NONE)


def delete_duplicates(conn, docs, unique_key, f):
    backup = []
    for doc in docs:
        d = list(conn.find({unique_key: doc['_id']}).sort([("updated_at", DESCENDING)]))
        uid = d[0]['_id']
        value = d[0][unique_key]
        conn.delete_many({"_id": {"$ne": uid}, unique_key: value})
        for i in d:
            backup.append(i)
    f.write(str(backup))

def perform_db_ops(conn, unique_key, f):
    key = "$"+unique_key
    docs = list(conn.aggregate([
                {"$group": {"_id": key, "count": {"$sum": 1}}},
                {"$match": {"_id": {"$ne": None}, "count": {"$gt": 1}}}
            ]))
    delete_duplicates(conn, docs, unique_key, f)


if __name__=="__main__":
    conn = mongo_conn["jds"]["buscojobs"]
    unique_key = "detail_url"
    f = open("/Users/manojbb/Desktop/backup/buscojobs"+".txt", "a")
    perform_db_ops(conn, unique_key, f)


# def delete_duplicates_new(conn, docs, unique_key, f):
#     backup = []
#     for doc in docs:
#         d = list(conn.find({unique_key: doc['_id']['course_id']}).sort([("updated_at", DESCENDING)]))
#         uid = d[0]['_id']
#         value = d[0][unique_key]
#         conn.delete_many({"_id": {"$ne": uid}, unique_key: value})
#         for i in d:
#             backup.append(i)
#     f.write(str(backup))


# if __name__=="__main__":
#     conn = mongo_conn["courses"]["udemy"]
#     unique_key = "id"
#     docs = list(conn.aggregate([
#         {
#             "$group": {
#                 "_id": {"course_id": "$id", "detail_url": "$detail_url"},
#                 "total_docs": {"$sum": 1}
#             }
#         },
#         {
#             "$match": {
#                 "total_docs": {"$gt": 1}
#             }
#         }
#     ]))
#     f = open("/Users/manojbb/Desktop/backup/udemy"+".txt", "a")
#     delete_duplicates_new(conn, docs, unique_key, f)
