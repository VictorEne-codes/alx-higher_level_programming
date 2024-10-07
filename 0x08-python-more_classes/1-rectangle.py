#!/usr/bin/python3
"""empty class Rectangle that defines a rectangle:"""


class Rectangle:
    """empty class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes the rectangel class

        Args:
            width: input
            height: input
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """width of the rectange

        Returns: width
        """
        return self._width

    @property
    def height(self):
        """height of the rectangle

        Returns: height
        """
        return self._height

    @width.setter
    def width(self, value):
        """property setter for width

        Args:
            value: width
        Raises:
            TypeError: if width is not integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @height.setter
    def height(self, value):
        """property setter for height

        Args:
            value: height
        Raises:
            TypeError: if height is not integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
