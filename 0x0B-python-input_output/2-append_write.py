#!/usr/bin/python3
""" Defines a file-appending function """


def append_write(filename="", text=""):
    """ A function that appends a string at the end of a text file (UTF8)
    and returns the number of characters written """
    with open(filename, 'a', encoding="utf-8") as f:
        nb_characters = f.write(text)

    return nb_characters
