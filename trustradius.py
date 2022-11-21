# from datetime import datetime
#
# uri = "mongodb://mongoreader:1f2d1e2e67df@qa-mongo.draup.technology:27017/admin"
#
# mongo_conn = MongoClient(uri, connect=False, ssl_cert_reqs=ssl.CERT_NONE)
#
# coll = mongo_conn["metadata"]["consul_conal_conference"]
#
# data = list(coll.find({"flags":{"$exists": True}}))
# sum = 0
# for i in data:
#     current_page = i["flags"]["conal_conference_alerts_events_v1_events_listing"]["current_page"]
#     if current_page > 5:
#         sum += (current_page-5) + 1
#     else:
#         sum += 1
# print(sum)

#sources = ["consul_conal_conference", "consul_apple", "consul_catho", "consul_amazon", "consul_flexcareers", "intermediary_meta.meta_apple_jds", "intermediary_meta.meta_conal_conference_alerts_events_v1_events"]

# from pymongo import MongoClient
# import ssl
# from utils.db_ops import connect_to_coll
#
#
# def get_metrics():
#     from utils.report.queries import get_total_pages_query
#     from utils.report import get_final_page_stats
#     sources_list = ["conal_conference_alerts_events_v1_events_listing"]
#     coll1 = connect_to_coll("workflow", "harvester_config")
#     final_list = []
#     for source in sources_list:
#         doc = coll1.find_one({"task": source})
#         input_collection = doc.get("producer", {}).get("collections", {}).get("input_collection")
#         db, coll = input_collection.split(".")
#         conn = connect_to_coll(db, coll)
#         query = get_total_pages_query(source)
#         data = list(conn.aggregate(query))[0]
#         total_processed_pages, total_pages_count, total_pages_exists_false_count = get_final_page_stats(data, "PageNumber")
#         final_list.append(dict(total_processed_pages=total_processed_pages, total_pages_count=total_pages_count,
#                                total_pages_exists_false_count=total_pages_exists_false_count))
#     print("")
#     print(final_list)
#
#
# get_metrics()
