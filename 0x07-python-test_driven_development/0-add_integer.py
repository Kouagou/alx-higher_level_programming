#!/usr/bin/python3
"""
    Add two integers.
"""


def add_integer(a, b=98):
    """ A function that adds 2 integers.

    Args:
        a: Firt parameter.
        b: Second parameter. Default to 98.

    Returns:
        Sum of the two integers.

    Raises:
        TypeError: If either of the arguments are not an integer or a float.

    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
