#!/usr/bin/python3
"""
Module 4-inherits_from.py

Contains method inherits_from
returns True if obj is instance of class it inherits from
or its subclass of
"""


def inherits_from(0bj, a_class):


    """
    use type() to get specific class
    use isinstance() to get class and any parent classes too
    use issubclass() to get what object is a subclass of 
    """
    if (type(obj) == a_class):
        return False
    return isinstance(obj, a_class)
