#!/usr/bin/python3
"""funtion to add two integers"""


def add_integer(a, b=98):
    """this add two integers.

    Args:
        a: input.
        b: input.

    Return: addition

    Raises:
        TypeError: if a is an integer
        TypeError: if b is an integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
