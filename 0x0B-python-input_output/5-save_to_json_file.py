#!/usr/bin/python3
"""write object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """object to text file in json format"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
