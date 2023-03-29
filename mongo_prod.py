from sshtunnel import SSHTunnelForwarder
from pymongo import MongoClient
from datetime import datetime
import ssl
ssh_session_db = SSHTunnelForwarder(
    ssh_address_or_host='3.128.8.200',
    ssh_username='manoj',
    ssh_pkey='/Users/manojbb/Documents/id_rsa',
    ssh_private_key_password='draup',
    ssh_port=22,
    remote_bind_address=('qa-mongo-private.draup.technology', 27017),
    local_bind_address=('127.0.0.1', 27019)
)
ssh_session_db.start()
print("Local Bind Port: ", ssh_session_db.local_bind_port)
m_conn = MongoClient(host='127.0.0.1',
                     port=27019,
                     username='mongoadmin',
                     password='1f2d1e2e67df')

uri1 = "mongodb://localhost:27017"
mongo_conn1 = MongoClient(uri1, connect=False, ssl_cert_reqs=ssl.CERT_NONE)


def update_layoff():
    source_coll = mongo_conn1['metadata']['consul_naukri']
    target_coll = m_conn["metadata"]["consul_naukri_v1"]
    docs = list(source_coll.find({}))
    print(len(docs))
    count = 1
    for doc in docs:
        print(count)
        del doc['_id']
        doc['updated_at'] = datetime.now()
        target_coll.update_one({"keyword": doc["keyword"]}, {"$set": doc}, upsert=True)
        count += 1


def update_layoff_employees():
    source_coll = mongo_conn1['harvests']['layoff_employees']
    target_coll = m_conn['harvests']['layoff_employees']
    docs = list(source_coll.find({}))
    print(len(docs))
    count = 1
    for doc in docs:
        print(count)
        del doc['_id']
        doc['updated_at'] = datetime.now()
        target_coll.update_one({"id": doc["id"]}, {"$set": doc}, upsert=True)
        count += 1


def update_bls_city_meta():
    source_coll = mongo_conn1['demographics']['temp_old']
    target_coll = m_conn['metadata']['consul_bls_city']
    docs = list(source_coll.find())
    count = 1
    for doc in docs:
        target_coll.insert_one({"location": doc['location'], 'type': doc['type'], 'link': doc['link'], "created_at": datetime.now(), "updated_at": datetime.now()})
        print(count)
        count += 1


if __name__ == "__main__":
    update_layoff()
