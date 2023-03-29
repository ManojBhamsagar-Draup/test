from system.db.factory import DBFactory
from system.logger.factory import LoggerFactory
import requests

logger = LoggerFactory.create(name='LayoffDetails')
logger_context = "LayoffDetails"

DB_MANAGER = DBFactory.create()()
DB_MANAGER._create_connection()

REQUEST_URL = "https://sheets.googleapis.com/v4/spreadsheets/1ffu4J_b0g2B4YLo7xvls3U2turNuS-QB2Khv5Qcrlrk/?key=AIzaSyC0P8q07pfEpXXTpPTGrVEP2fsA_sWn0-U&includeGridData=true&prettyPrint=true"


def check_linkedin_column(row):
    if not row:
        return False, []
    columns = []
    for i in range(len(row)):
        columns.append(row[i].get('formattedValue'))
    for col in columns:
        try:
            if "linked" in col.lower():
                return True, columns
        except Exception as e:
            print(repr(e))
            continue
    return False, columns


def get_sheet_columns(rows, index):
    column_check_length = index + 7

    for check_index in range(index, column_check_length):
        flag = False
        columns = []
        if check_index < len(rows):
            row = rows[check_index].get('values')
            flag, columns = check_linkedin_column(row)
        if flag:
            return check_index, columns
    return None, []


def get_sheet_data(sheet_data):
    start_row_index = sheet_data.get('properties', {}).get('gridProperties', {}).get('frozenRowCount', 1)
    sheet_length = len(sheet_data.get('data', [])[0].get('rowData', []))
    if sheet_length <= 0:
        return []
    rows = sheet_data.get('data', [])[0].get('rowData', [])
    sheet_data = []
    new_index, columns = get_sheet_columns(rows, start_row_index - 1)
    if not columns or start_row_index is None:
        return sheet_data
    start_row_index = new_index + 1
    for index in range(start_row_index, sheet_length):
        row = dict()
        temp = None
        for i in range(len(columns)):
            col_name = columns[i]
            try:
                temp = rows[index].get('values')[i].get('formattedValue')
            except Exception as e:
                print(repr(e))
            if temp:
                row[col_name] = temp
        sheet_data.append(row) if row else False
    return sheet_data


def get_sheets(data):
    if not data.get('sheets', []):
        return None
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


def clean_scraped_data(unclean_data):
    for data in unclean_data:
        if data.get(None):
            del data[None]
    return unclean_data


if __name__ == '__main__':
    SOURCE_DB_NAME = "harvests"
    SOURCE_COLL_NAME = "layoff_employees"

    DB_MANAGER.set_collection(SOURCE_DB_NAME, SOURCE_COLL_NAME)
    FIND_CONDITION = {"employee_details": {"$exists": False}}

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
            scraped_data = clean_scraped_data(scraped_data)
            final_data = {"employee_details": scraped_data}
            _filter = {"harvesting_link": sheet_url}
            update_record(_filter, final_data)
