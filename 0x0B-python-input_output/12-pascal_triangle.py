#!/usr/bin/python3
""" Pascal's Triangle. """


def pascal_triangle(n):
    """ A function that return a list of lists of integers
    representing the Pascal’s triangle of n."""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tr = triangles[-1]
        temp = [1]
        for i in range(len(tr) - 1):
            temp.append(tr[i] + tr[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
