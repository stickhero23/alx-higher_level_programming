#!/usr/bin/python3
"""
The function returns True if the object of an intance of, or an
instance of inherited class.
"""
def is_kind_of_class(obj, a_class):
    """ returns True or False """
    return isinstance(obj, a_class)
