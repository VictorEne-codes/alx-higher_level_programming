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


    def __str__(self):
        """pribt out """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
