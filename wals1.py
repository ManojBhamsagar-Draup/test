def get_data(data, **kwargs):
    doc_list = data["result"]["aaData"]
    doc_dict = []

    for doc in doc_list:
        temp = ""
        temp_dict = dict()
        for ele in doc:
            temp += ele
        temp_dict["key"] = temp
        doc_dict.append(temp_dict)
    data["result"]["aadata"] = doc_dict
    return data


def _update_variables(url, request_params, query_variables, payload):
    request_params.update({"url": url})
    if payload and request_params.get('payload'):
        request_params.update({"payload": payload})
    query_variables.update({"requestParams": request_params})