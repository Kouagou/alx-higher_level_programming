#!/usr/bin/python3
""" LockedClass """


class LockedClass:
    """ Only allows instatiation of an attribute called first_name """

    __slots__ = ["first_name"]
