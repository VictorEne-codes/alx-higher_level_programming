#!/usr/bin/python3
"""based on task 5"""


class BaseGeometry:
    """a new class"""

    def area(self):
        """raise an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer

        Args:
            name: input
            value: input

        Raises:
            TypeError: if not integer
            ValueError: if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherut class"""

    def __init__(self, width, height):
        """initialise class

        Args:
            width: input
            height: input
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculates area of a rectangle.

        Returns:
            int: area.
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of the rectangle.

        Returns:
            str: string representation of rectangle.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """inherut class"""

    def __init__(self, size):
        """initialise class

        Args:
            size: input
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates area of a quare.

        Returns:
            int: area.
        """
        return self.__size * 2
