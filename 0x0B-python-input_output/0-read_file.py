#!/usr/bin/python3
"""function to read file"""


def read_file(filename=""):
    """function to read file"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
