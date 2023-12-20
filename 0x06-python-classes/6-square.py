#!/usr/bin/python3
# 0-square.py by Kenneth K. N'TCHA
"""Defines a square """


class Square:
    """A class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
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

        if type(position) is not tuple or len(position) != 2 or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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
        position should be use by using space -
        Don’t fill lines by spaces when position[1] > 0
        """

        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """Retrieve the position value"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set position value
        Args:
            value - the new value to be set
        """

        if type(value) is not tuple or len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
