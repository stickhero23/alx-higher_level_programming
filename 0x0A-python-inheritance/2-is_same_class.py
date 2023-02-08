#!/usr/bin/python3
""" Program that validates an object """


def is_name_class(obj, a_class):
    """ returns True or False """
    if (type(obj) == a_class):
        return True
    return False
