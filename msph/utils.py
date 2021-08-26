import json

def format_json(dict_):
    return json.dumps(dict_, indent=4, ensure_ascii=False)
