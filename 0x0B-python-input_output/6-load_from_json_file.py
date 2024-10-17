#!/usr/bin/python3
"""from json to objects"""
import json


def load_from_json_file(filename):
    """json to objects"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
