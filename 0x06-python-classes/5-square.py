#!/usr/bin/python3
# 0-square.py by Kenneth K. N'TCHA
"""Defines a square """


class Square:
    """A class Square that defines a square"""

    def __init__(self, size=0):
        """Instantiation with size (no type/value verification)
        Args:
            size - represent the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculate the square area
        Returns:
            the current square area
        """

        return (self.__size * self.__size)

    @property
    def size(self):
        """Retrieve the size value"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set size value
        Args:
            value - the new value to be set
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #

        If size is equal to zero, print an empty line.
        """

        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
