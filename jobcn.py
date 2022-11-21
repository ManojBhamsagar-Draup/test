from pymongo import MongoClient
import ssl
from datetime import datetime

uri = "mongodb://localhost:27017"

mongo_conn = MongoClient(uri, connect=False, ssl_cert_reqs=ssl.CERT_NONE)

coll = mongo_conn["metadata"]["consul_jobcn"]

data = [{"location": "Anhui", "code": "24"},
        {"location": "Macao", "code": "44"},
        {"location": "Beijing", "code": "11"},
        {"location": "Chongqing", "code": "14"},
        {"location": "Fujian", "code": "28"},
        {"location": "Guangdong", "code": "30"},
        {"location": "Guangxi", "code": "31"},
        {"location": "Gansu", "code": "35"},
        {"location": "Guizhou", "code": "33"},
        {"location": "foreign", "code": "45"},
        {"location": "Hunan", "code": "29"},
        {"location": "Hubei", "code": "26"},
        {"location": "Henan", "code": "22"},
        {"location": "Hebei", "code": "18"},
        {"location": "Heilongjiang", "code": "15"},
        {"location": "Hainan", "code": "41"},
        {"location": "Jilin", "code": "16"},
        {"location": "Jiangsu", "code": "23"},
        {"location": "Jiangxi", "code": "27"},
        {"location": "Liaoning", "code": "17"},
        {"location": "Inner Mongolia", "code": "19"},
        {"location": "Ningxia", "code": "37"},
        {"location": "Qinghai", "code": "38"},
        {"location": "Shanghai", "code": "13"},
        {"location": "Shandong", "code": "20"},
        {"location": "Shanxi", "code": "21"},
        {"location": "Shaanxi", "code": "36"},
        {"location": "Sichuan", "code": "34"},
        {"location": "Tianjin", "code": "12"},
        {"location": "Taiwan", "code": "42"},
        {"location": "Tibet", "code": "40"},
        {"location": "Hongkong", "code": "43"},
        {"location": "Xinjiang", "code": "39"},
        {"location": "Yunnan", "code": "32"},
        {"location": "Zhejiang", "code": "25"}]

for i in data:
    i['created_at'] = datetime.now()
    i['updated_at'] = datetime.now()

for i in data:
    coll.insert_one(i)