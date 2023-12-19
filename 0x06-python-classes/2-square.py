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
