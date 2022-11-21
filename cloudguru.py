def get_vendors(data, **kwargs):
    vendors = []
    vendors_data = data.get("result").get("results")[0].get("facets").get("vendors")
    for vendor, value in vendors_data.items():
        vendors.append({"vendor": vendor})

    data["result"]["results"][0]["facets"]["added_vendors"] = vendors
    return data
