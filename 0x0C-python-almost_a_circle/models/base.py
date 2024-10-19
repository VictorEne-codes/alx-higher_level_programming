#!/busr/bin/python3
"""creating a base class"""


class Base:
    """new class called base"""
    __nb_objects = 0
    def __init__(self, id=None):
        """initialises the class

        Args:
            id: input
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
