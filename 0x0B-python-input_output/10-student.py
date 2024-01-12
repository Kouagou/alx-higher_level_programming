#!/usr/bin/python3
""" Student to JSON """


class Student:
    """ Defines a Student class """
    def __init__(self, first_name, last_name, age):
        """ Instanciation
        Args:
            first_name - The firstname of the student.
            last_name - The lastname of the student.
            age - The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if type(attrs) == list and all(isinstance(i, str) for i in attrs):
            # return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
