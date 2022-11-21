def get_data_list(data, **kwargs):
    layoff = data.get("result", {}).get("data", {}).get("rows", [])
    location_codes = data.get("result", {}).get("data", {}).get("columns", [])[4].get("typeOptions", {}).get("choices", {})

    for item in layoff:
        locations = list()
        for location in item.get("cellValuesByColumnId", {}).get("fld2D71rjOAW8NZuF", {}):
            locations.append(location_codes.get(location).get("name"))
        item["locations"] = locations

    data["result"]["data"]["layoff"] = layoff
    return data
