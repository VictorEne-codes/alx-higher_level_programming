#!/usr/bin/python3
"""a new class for square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """inistaling new  class square

        Args:
            size: input
            x: i
            y: input
            id: input
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value


    def __str__(self):
        """pribt out """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """argument variables"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        if len(args) == 0:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                if key == "id":
                    self.id = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
