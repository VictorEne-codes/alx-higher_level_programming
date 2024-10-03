#!/usr/bin/python3
"""Define class suare with init size"""

class Square:
    """defineing a class square"""
    def __init__(self, size=0):
        """initialize self"""
        self._size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
