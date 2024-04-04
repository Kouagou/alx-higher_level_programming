#!/usr/bin/python3
""" Define a function that find a peak. """


def find_peak(list_of_integers):
    """
        Args:
            list_of_integers(int): list of integers to find peak of
        Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)

    start = 0
    end = size - 1

    if size == 0:
        return None

    while start <= end:
        mid = (start + end) // 2

        if ((mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1])
            and (mid == size - 1 or
                 list_of_integers[mid] >= list_of_integers[mid + 1])):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return None
