#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private attribute size
"""


class Square:
    """
    Definition of class Square

    Args:
        size : size of a side in square
    """
    def __init__(self, size):
        """
        Initializes square

        Attributes:
            sieze: size of a side of square
        """
        self.__size = size
