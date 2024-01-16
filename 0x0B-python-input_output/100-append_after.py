#!/usr/bin/python3
""" This module defines a Search and update in a file. """


def append_after(filename="", search_string="", new_string=""):
    """ A function that inserts a line of text to a file,
    after each line containing a specific string. """
    text = ""
    with open(filename, 'r+') as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
        f.write(text)
