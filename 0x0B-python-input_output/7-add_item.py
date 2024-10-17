#!/usr/bin/python3
"""adds element yo python list"""
from sys import argv


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


try:
    new_list = load('add_item.json')
except (ValueError, FileNotFoundError):
    new_list = []

for i in argv[1:]:
    new_list.append(i)
save(new_list, 'add_item.json')
