from pymongo import MongoClient
import ssl
from datetime import datetime
import json
uri1 = "mongodb://localhost:27017"
#
mongo_conn1 = MongoClient(uri1, connect=False, ssl_cert_reqs=ssl.CERT_NONE)
#
source_coll = mongo_conn1['metadata']['consul_careerbuilder_test']

f = open('consul_job_roles.json')


data_job = json.load(f)

f = open('consul_careerbuilder.json')

data_loc = json.load(f)

for job in data_job:
    for loc in data_loc:
        job_role = job['job_role']
        location = loc['state']
        query_path = f"/jobs?keywords={job_role}&location={location}"
        source_coll.update(
            {"query_path": query_path},
            {"query_path": query_path, "job_role": job_role, "location": location, "created_at": datetime.now(), "updated_at": datetime.now()},
            upsert=True)
