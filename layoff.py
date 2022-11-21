from system.db.factory import DBFactory
import pandas as pd

DB_MANAGER = DBFactory.create()()
DB_MANAGER._create_connection()


def modify_url(sheet_url):
    try:
        url = sheet_url + "/export?format=csv"
    except Exception as e:
        print(repr(e))
        return None
    return url


def check_columns(cols):
    flag = False
    no_cols = False
    sample_colnames = ["linkedin", "location"]
    for col in cols:
        try:
            col = col.lower()
        except Exception as e:
            print(repr(e))
            print(f"cannot convert {col} to lower")
            continue
        if any(sample_colname in col for sample_colname in sample_colnames):
            flag = True
            if "linkedin.com" in col:
                no_cols = True
            return [flag, no_cols]
    return [flag, no_cols]


def generate_column_names(num_cols):
    generated_column_names = []
    for i in range(num_cols):
        generated_column_names.append('column' + str(i))
    return generated_column_names


def read_data(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        print(repr(e))
        return None


def perform_df_operations(url):
    df = read_data(url)
    if df is None or df.empty:
        return None

    flag = False
    no_cols = False
    count = df.shape[0]

    while count > 1:
        cols = list(df.columns)
        flag, no_cols = check_columns(cols)

        if not flag:
            new_header = df.iloc[0]
            df = df[1:]
            df.columns = new_header
            count -= 1
        else:
            break

    if flag and no_cols:
        col_name = generate_column_names(df.shape[1])
        df.columns = col_name

    df = df.dropna(axis=1, how='all')
    df.reset_index(inplace=True, drop=True)
    return df


def update_record(_filter, df):
    employee_list = []
    for index, rows in df.iterrows():
        try:
            employee_list.append(df.iloc[index].to_dict())
            update = {"employees_details": employee_list}
            DB_MANAGER._update_one(filter=_filter, update=update, upsert=True)
        except Exception as e:
            print(repr(e))


def layoff_employee_details():
    SOURCE_DB_NAME = "harvests"
    SOURCE_COLL_NAME = "layoff_employees"

    DB_MANAGER.set_collection(SOURCE_DB_NAME, SOURCE_COLL_NAME)
    FIND_CONDITION = {"link": {"$exists": True}}

    doc_list = list(DB_MANAGER._find(FIND_CONDITION))

    for ele in doc_list:
        sheet_url = ele.get("harvesting_link", "")
        url = modify_url(sheet_url)

        if not url:
            continue

        df = perform_df_operations(url)

        if df is None or df.empty:
            continue

        _filter = {"name": ele["name"]}
        update_record(_filter, df)


layoff_employee_details()
