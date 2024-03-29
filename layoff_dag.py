from system.db.factory import DBFactory
from system.logger.factory import LoggerFactory
import requests

logger = LoggerFactory.create(name='LayoffDetails')
logger_context = "LayoffDetails"

DB_MANAGER = DBFactory.create()()
DB_MANAGER._create_connection()

REQUEST_URL = "https://sheets.googleapis.com/v4/spreadsheets/1ffu4J_b0g2B4YLo7xvls3U2turNuS-QB2Khv5Qcrlrk/?key=AIzaSyC0P8q07pfEpXXTpPTGrVEP2fsA_sWn0-U&includeGridData=true&prettyPrint=true"


def get_final_doc(validated_doc) -> dict:
    if not validated_doc:
        return {}
    final_doc = dict()
    for index in range(len(validated_doc)):
        final_doc[str(index)] = validated_doc[index].get('formattedValue', None)
    return final_doc


def validate_row(data) -> dict:
    if not data:
        return {}
    linkedin_flag = False
    for item in data:
        try:
            if "linkedin.com/in" in item.get('formattedValue', "").lower():
                linkedin_flag = True
                break
        except Exception as e:
            print(repr(e))
    return get_final_doc(data) if linkedin_flag else {}


def get_sheet_data(sheet_data) -> list:
    start_row_index = sheet_data.get('properties', {}).get('gridProperties', {}).get('frozenRowCount', 1)
    sheet_length = len(sheet_data.get('data', [])[0].get('rowData', []))
    if sheet_length <= 0:
        return []
    rows = sheet_data.get('data', [])[0].get('rowData', [])
    sheet_data = []

    for index in range(start_row_index, sheet_length):
        validated_doc = dict()
        try:
            row = rows[index].get('values', [])
            validated_doc = validate_row(row)
        except Exception as e:
            print(repr(e))
        sheet_data.append(validated_doc) if validated_doc else False
    return sheet_data


def get_sheets(data) -> list:
    if not data.get('sheets', []):
        return []
    sheets_data = []
    sheets = data.get('sheets', [])
    for sheet in sheets:
        sheet_data = get_sheet_data(sheet)
        if sheet_data:
            sheets_data.extend(sheet_data)
    return sheets_data


def get_sheet_id(sheet_url_input):
    try:
        return sheet_url_input.split("d/")[-1] if "d/" in sheet_url else ""
    except Exception as e:
        print(repr(e))
    return ""


def update_record(_filter, employee_list):
    try:
        update = employee_list
        DB_MANAGER._update_one(filter=_filter, update=update, upsert=True)
    except Exception as e:
        logger._exception_mixin(msg=f"cannot update record {repr(e)}", context=logger_context)


if __name__ == '__main__':
    SOURCE_DB_NAME = "harvests"
    SOURCE_COLL_NAME = "layoff_employees"

    DB_MANAGER.set_collection(SOURCE_DB_NAME, SOURCE_COLL_NAME)
    FIND_CONDITION = {"harvesting_link": {"$exists": True}}

    doc_list = list(DB_MANAGER._find(FIND_CONDITION))
    count = 1
    for doc in doc_list:
        print(count)
        count += 1

        sheet_url = doc["harvesting_link"]
        sheet_id = get_sheet_id(sheet_url)
        if not sheet_id:
            pass

        request_url = "https://sheets.googleapis.com/v4/spreadsheets/{0}/?key=AIzaSyC0P8q07pfEpXXTpPTGrVEP2fsA_sWn0-U&includeGridData=true&prettyPrint=true".format(sheet_id)
        resp = None
        try:
            print("requesting url {0}".format(sheet_url))
            resp = requests.get(url=request_url)
        except Exception as e:
            print("invalid response {0}".format(sheet_url))
        if resp.status_code != 200:
            print("status code is {0} for url {1}".format(resp.status_code, sheet_url))
            continue
        resp_data = resp.json()
        scraped_data = []
        try:
            scraped_data = get_sheets(resp_data)
        except Exception as e:
            print("exception for url {0}".format(sheet_url))
        if scraped_data:
            final_data = {"employees_details": scraped_data}
            _filter = {"harvesting_link": sheet_url}
            update_record(_filter, final_data)
