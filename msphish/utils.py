import json

def format_json_string(dict_):
    return json.dumps(dict_, indent=4, ensure_ascii=False)

def write_to_file(path:str, data,):
    with open(path, 'w') as file:
        file.write(data)