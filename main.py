from pymongo import MongoClient
import pandas as pd

conn_uri = "mongodb://localhost:27017"
unable = []
def get_employees_details(conn_uri):
    conn = MongoClient(conn_uri)
    SOURCE_DB_NAME = "harvests"
    SOURCE_COLL_NAME = "layoff_employees"
    db1 = conn[SOURCE_DB_NAME]
    coll1 = db1[SOURCE_COLL_NAME]
    FIND_CONDITION = {"link": {"$exists": True}}
    doc_list = list(coll1.find(FIND_CONDITION))
    list_count = 1
    for ele in doc_list:
        print(list_count)
        list_count += 1
        sheet_url = ele.get("harvesting_link", "")
        try:
            url = sheet_url + "/export?format=csv"
        except Exception as e:
            print(repr(e))
            continue
        try:
            df = pd.read_csv(url)
            flag = False
            no_cols = False

            sample_colnames = ["linkedin", "location"]
            count = df.shape[0]
            while count > 1:
                cols = list(df.columns)
                for col in cols:
                    try:
                        col = col.lower()
                    except Exception as e:
                        print(repr(e))
                        print(f"cannot conver {col} to lower")
                        continue
                    if any(sample_colname in col for sample_colname in sample_colnames):
                        flag = True
                        if "linkedin.com" in col:
                            no_cols = True
                        break
                if not flag:
                    new_header = df.iloc[0]  # grab the first row for the header
                    df = df[1:]  # take the data less the header row
                    df.columns = new_header
                else:
                    break

            if flag and no_cols:
                generated_columns_names = []
                for i in range(df.shape[1]):
                    generated_columns_names.append('column'+str(i))
                df.columns = generated_columns_names

            df = df.dropna(axis=1, how='all')
            df.reset_index(inplace=True, drop=True)
            employee_list = []
            for index, rows in df.iterrows():
                employee_list.append(df.iloc[index].to_dict())
                coll1.update_one(
                    {
                        "id": ele["id"]
                    },
                    {
                        "$set": {
                            "employees_details": employee_list,
                        }
                    },
                    upsert=True
                    )
        except Exception as e:
            print(repr(e))
            unable.append(sheet_url)
            print(f"couldn't get employee data from sheet url: {sheet_url}")

    conn.close()

get_employees_details(conn_uri)
print("printing unable")
for i in unable:
    print(i)
