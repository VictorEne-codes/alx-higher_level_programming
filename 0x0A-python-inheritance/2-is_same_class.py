#!/usr/bin/python3
"""function to check if exactly an insyance"""


def is_same_class(obj, a_class):
    """function to check if instance

    Args:
        obj: input
        a_class: input

    Returns: True
    """

    return type(obj) == a_class
