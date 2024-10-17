#!/usr/bin/python3
"""create a class student"""


class Student:
    """create a class"""

    def __init__(self, first_name, last_name, age):
        """initialise class

        Args:
            first_name: input
            ladt_name: input
            age: input
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """class tk json"""
        return self.__dict__
