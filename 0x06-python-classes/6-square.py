#!/usr/bin/python3
"""
Square Class: Prints a square with # and coordinates
"""


class Square:
    """ clas square that defines a square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the attributes"""
        self.size = size
        self.position = position


    @property
    def size(self):
        """ get size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size with safe Assignment """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ retrieve the initial position """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the new position """
        s = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(s)
        elif (len(value) != 2):
            raise TypeError(s)
        else:
            for t in value:
                if (t < 0):
                    raise TypeError(s)
                elif (type(t) is not int):
                    raise TypeError(s)
        self.__position = value

    def area(self):
        """ Return the area of the square """
        return (self.__size * self.__size)

    def my_print(self):
        """ prints in stdout with # """
        if (self.size != 0):
             print("\n" * self.__position[1], end="")
             print("\n".join([" " * self.__position[0] + "#" * self.__size
                 for rows in range(self.__size)]))
        else:
            print("")
