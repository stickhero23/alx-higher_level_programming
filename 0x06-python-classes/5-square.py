#!/usr/bin/python3
"""
Module 5-square
Defines class Square with private size and public area
Can access and update size
"""


class Square:
    """ class Square definition """
    def __init__(self, size=0):
        """ Initialize attributes """
        self.size = size

    @property
    def size(self):
        """ gets the size """
        return self.__size

    @size.setter
    def size(self, size)
        """ Value: sets size to value, if int and >= 0 """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculate the area of square """
        return (self.__size * self.__size)
    
    def my_print(self):
        """ prints in stdout the square using # """
         print("\n".join(["#" * self.__size for rows in range(self.__size)]))
