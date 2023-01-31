#!/usr/bin/python3
"""
Program prints the name withe edge cases
"""


def say_my_name(first_name, last_name=""):
    """ The function prints my name"""
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last name must be a string")
    print("My name is {:s}".format(first_name, last_name))
