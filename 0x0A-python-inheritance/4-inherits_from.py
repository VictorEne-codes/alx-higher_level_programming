#!/usr/bin/python3
"""function to check if instance of inherited class"""


def inherits_from(obj, a_class):
    """check if inherited class

    Args:
        obj: input
        a_class: input

    Returns:
        boolean: true of false
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
