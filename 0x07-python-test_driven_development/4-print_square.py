#!/usr/bin/python3
"""
Program prints a square with # on given input
"""


def print_square(size):
    """ function prints a square using # symbol"""
    msg = "size must be an integer"
    if not (isinstance(size, int)):
        raise TypeError(msg)
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (isinstance(size, float) and size < 0):
        raise TypeError(msg)
    for x in range(size):
        for y in range(size):
            print("#", end='')
        print('')
