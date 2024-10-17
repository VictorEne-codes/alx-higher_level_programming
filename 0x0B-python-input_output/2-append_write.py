#!/usr/bin/python3
"""function to append to file"""


def append_write(filename="", text=""):
    """funtion to write"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
