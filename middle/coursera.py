import re
import json


def get_data(data, **kwargs):
    pattern = "(window.__APOLLO_STATE__ = )(.*)(; window.renderedClassNames = )"
    data = re.split(pattern, data)[2]
    data = '{"data":[{"Innerdata":' + data + '}]}'
    return data
