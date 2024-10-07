#!/usr/bin/python3
"""function to create squares."""


def print_square(size):
    """prints a square with the character #.

    Args:
        size: size of square

    Return: A square of $

    Raises:
        TypeError: if size if not integer
        ValueError: if size if < 0
        TypeError: if size is a float
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)
