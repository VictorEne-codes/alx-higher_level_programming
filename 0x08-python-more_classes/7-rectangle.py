#!/usr/bin/python3
"""empty class Rectangle that defines a rectangle:"""


class Rectangle:
    """empty class Rectangle that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the rectangel class

        Args:
            width: input
            height: input
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """width of the rectange

        Returns: width
        """
        return self.__width

    @property
    def height(self):
        """height of the rectangle

        Returns: height
        """
        return self.__height

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
            self.__width = value

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
            self.__height = value

    def area(self):
        """area of the rectange

        Returs: area
        """

        return self.__width * self.__height

    def perimeter(self):
        """perimeter of the rectangle

        Returns: perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the rectangle with the character # .

        Returns: str
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")
        rectangle.pop()
        return "".join(rectangle)

    def __repr__(self):
        """ return a string representation of the rectangle

        Returns: repr
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """return instance of rectangele deleted"""

        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1
