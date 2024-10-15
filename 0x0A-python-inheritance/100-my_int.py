#!/usr/bin/python3
"""inherit class"""


class MyInt(int):
    """Defines a class MyInt.

    Args:
        int (int): value
    """
    def __init__(self, value):
        """Creates new instances of class MyInt.

        Args:
            value: input
        """
        self.__value = value

    def __eq__(self, other):
        """The method equal

        Args:
            other: input

        Returns:
            boolean: True or False.
        """
        return self.__value != other

    def __ne__(self, other):
        """The method not equal

        Args:
            other: input

        Returns:
            boolean: True or False
        """
        return self.__value == other
