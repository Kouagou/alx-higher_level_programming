#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ A function that returns a list of lists of integers
    representing the Pascal’s triangle of n. """

    if n <= 0:
        return []
    pascal = []
    for i in range(n):
        tmp_list = []
        for j in range(i + 1):
            tmp_list.append(combinatorial(i, j))
        pascal.append(tmp_list)

    return pascal


def factoriel(n):
    """ This function is defined to compute the factoriel of a number """
    if n == 0:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def combinatorial(n, p):
    """ This function is defined to compute the combinatorics of p in n """
    return int(factoriel(n) / (factoriel(p) * factoriel(n - p)))
