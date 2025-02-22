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
