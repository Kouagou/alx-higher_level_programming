#!/usr/bin/python3
""" Defines a text file reading function """


def read_file(filename=""):
    """ Read a text file and prints it to stdout. """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
