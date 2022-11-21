def process_indicator_data(self, ind_data, year, cp_kwargs):
    ind_field = cp_kwargs[self.INDICATOR_FIELD]
    ind_db_key = cp_kwargs[self.INDICATOR_DB_KEY]
    year_str = str(year)
    page_last_updated = ind_data[0]["page_last_updated"]
    data = ind_data[0]["values"]
    for item in data:
        ind_value = item[ind_field]
        ind_key = ind_db_key + "_" + year_str
        item[ind_key] = ind_value
        item["page_last_updated"] = page_last_updated
        item.pop(ind_field)
    ind_data = ind_data[0]["values"]
    return ind_data

def get_data(doc, **kwargs):
    json_pagination = doc["result"][0]
    json_data = doc["result"][1]
    json_pagination["data"] = json_data
    doc["result"] = {"output": [json_pagination]}
    return doc
