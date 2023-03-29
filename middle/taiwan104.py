import re


def get_data(data, **kwargs):
    """
        extracts job_categories and area codes from scraped data
    """
    pattern = "(.*)(var PAGEVARS = )(.*)"
    if not data:
        return
    try:
        data = re.split(pattern=pattern, string=data)[3]
        final_data = '{"output":[' + data + ']}'
        return final_data
    except Exception as e:
        print(repr(e))
        return ""
