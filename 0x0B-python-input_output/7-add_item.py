#!/usr/bin/python3
"""adds element yo python list"""
from sys import argv


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


try:
    new_list = load('add_item.json')
except (ValueError, FileNotFoundError):
    new_list = []

new_list.extend(argv[1:])
save(new_list, 'add_item.json')
