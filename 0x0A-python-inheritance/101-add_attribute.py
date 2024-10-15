#!/usr/bin/python3
"""Funtion add_attribute"""


def add_attribute(object, attr_name, value):
    """Adds a new attribute to an object

    Args:
        object: input
        attr_name: input
        value: input
    
    Raises:
        TypeError:  if the object can’t have new attribute.
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attr_name, value)
