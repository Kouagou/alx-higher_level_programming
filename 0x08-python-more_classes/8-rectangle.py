#!/usr/bin/python3
""" Defines a Rectangle """


class Rectangle:
    """ Defines Rectangle
    Args:
        number_of_instances - for counting instances
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height
        Args:
            height - height of the rectangle
            width - width of the rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """ Returns the rectangle area """

        return self.width * self.height

    def perimeter(self):
        """ Returns the rectangle perimeter """

        if self.width == 0 or self.height == 0:
            return 0

        return (self.width + self.height) * 2

    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area ""
        Args:
            rect_1 - the first rentangle
            rect_2 - the second rectangle
        Raises:
            TypeError: if rect_1 or/and rect_2 is not an instance of Rectangle
        """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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

    def __str__(self):
        """ Print the rectangle with character # """

        if self.width == 0 or self.height == 0:
            return ""
        st = ""
        for i in range(self.height - 1):
            st += str(self.print_symbol) * self.width + "\n"
        st += str(self.print_symbol) * self.width
        return st

    def __repr__(self):
        """ Return a string representation of the rectangle """

        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """ Delete an instance """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
