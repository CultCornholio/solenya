import json
import argparse
import csv
from os import write

def format_json(dict_):
    return json.dumps(dict_, indent=4, ensure_ascii=False)

def save_json(dict_, path):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(dict_, file, indent=4, ensure_ascii=False)

def save_to_csv(rows, headers, path):
    with open(path, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
