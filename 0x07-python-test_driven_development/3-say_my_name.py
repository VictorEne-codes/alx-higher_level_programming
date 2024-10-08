#!/usr/bin/python3
"""Function to print name."""


def say_my_name(first_name, last_name=""):
    """prints full name.

    Args:
        first_name: input
        last_name: input

    Return: full name

    Raises:
        TypeError: if firstname is not a string
        TypeError: if lastname is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
