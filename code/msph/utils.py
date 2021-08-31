import json
import argparse

def format_json(dict_):
    return json.dumps(dict_, indent=4, ensure_ascii=False)

def save_json(dict_, path):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(dict_, file, indent=4, ensure_ascii=False)
