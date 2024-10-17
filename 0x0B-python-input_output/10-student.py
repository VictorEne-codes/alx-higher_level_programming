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

    def to_json(self, attrs=None):
        """from json to class"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict
