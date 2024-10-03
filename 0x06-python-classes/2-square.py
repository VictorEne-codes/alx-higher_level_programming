#!/usr/bin/python3
"""Define class suare with init size."""


class Square:
    """defineing a class square."""
    def __init__(self, size=0):
        """initialize self.

        Args:
            size(int): size of the square.
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
