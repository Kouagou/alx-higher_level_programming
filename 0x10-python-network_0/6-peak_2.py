#!/usr/bin/python3
""" Define a function that find a peak. """


def find_peak(list_of_integers):
    """
        Args:
            list_of_integers(int): list of integers to find peak of
        Returns: peak of list_of_integers or None
    """
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        peak = 0
        for i in range(len(list_of_integers)):
            if i == 0:
                if list_of_integers[i] >= list_of_integers[i + 1]:
                    peak = list_of_integers[i]
            elif i == (len(list_of_integers) - 1):
                if list_of_integers[i] >= list_of_integers[i - 1]:
                    peak = list_of_integers[i]
            else:
                if (list_of_integers[i] >= list_of_integers[i - 1] and
                        list_of_integers[i] >= list_of_integers[i + 1]):
                    peak = list_of_integers[i]
        return peak
