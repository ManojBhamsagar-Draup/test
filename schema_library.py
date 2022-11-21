from pymongo import MongoClient
import ssl
from datetime import datetime

uri = "mongodb://localhost:27017"

mongo_conn = MongoClient(uri, connect=False, ssl_cert_reqs=ssl.CERT_NONE)

coll = mongo_conn["workflow"]["harvester_schema_library"]

doc = {
	"scrapper_type" : "Products",
	"attributes": [
		{
			"attribute_name" : "product_name",
			"data_type" : "short text",
			"schema" : "string",
			"is_mandatory" : False
		},
		{
			"attribute_name" : "detail_url",
			"data_type" : "url",
			"schema" : "string",
			"is_mandatory" : False
		},
		{
			"attribute_name" : "overview",
			"data_type" : "long text",
			"schema" : "string",
			"is_mandatory" : False
		},
		{
			"attribute_name" : "product_logo",
			"data_type" : "url",
			"schema" : "string",
			"is_mandatory" : False
		},
		{
			"attribute_name" : "product_rating",
			"data_type" : "string/float",
			"schema" : ["string", "float"],
			"is_mandatory" : False
		},
		{
			"attribute_name" : "rating_tag",
			"data_type" : "short text",
			"schema" : "string",
			"is_mandatory" : False
		}
	],
	"created_at" : datetime.now(),
	"created_by" : "Manoj",
	"short_description" : "Extraction of product details from different products sources",
	"type_id" : 13
}

coll.insert_one(doc)
