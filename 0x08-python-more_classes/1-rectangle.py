#!/usr/bin/python3
""" Defines a Rectangle """


class Rectangle:
    """ Defines Rectangle """

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height
        Args:
            height - height of the rectangle
            width - width of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieve the width value """

        return self.__width

    @width.setter
    def width(self, value):
        """ Set width value
        Args:
            value - the new value to be set
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Retrieve the height value """

        return self.__height

    @height.setter
    def height(self, value):
        """ Set height value
        Args:
            value - the new value to be set
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value