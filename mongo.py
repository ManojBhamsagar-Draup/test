# from pymongo import MongoClient
# import ssl
# import pandas as pd
# from datetime import datetime
#
# uri1 = ""
#
# mongo_conn1 = MongoClient(uri1, connect=False, ssl_cert_reqs=ssl.CERT_NONE)
# source_coll = mongo_conn1['metadata']['consul_buscojobs']
#
# df = pd.read_csv('Job_Role.csv')
# count = 1
# for i in df.values:
#     print(count)
#     job_role = i[0].replace(" ", "-")
#     source_coll.insert_one({"job_role": job_role, "updated_at": datetime.now(), "created_at": datetime.now()})
#     count += 1


from pymongo import MongoClient
import ssl
from datetime import datetime


uri1 = "mongodb://draupreader:fqp6hf9DzFMvLRaN@mongodb1-harvestor.draup.technology:27017/admin"
uri2 = "mongodb://localhost:27017"

mongo_conn1 = MongoClient(uri1, connect=False, ssl_cert_reqs=ssl.CERT_NONE)
mongo_conn2 = MongoClient(uri2, connect=False, ssl_cert_reqs=ssl.CERT_NONE)

source_coll = mongo_conn1['metadata']['four_traders_companies']
target_coll = mongo_conn2['metadata']['four_traders_companies']

docs = list(source_coll.find({}).sort("_id", -1).limit(100))
count = 1

for doc in docs:
    count += 1
    print(count)
    target_coll.insert_one(doc)
    if count == 100:
        break