#!/usr/bin/python3
"""
Program that lookup all attributes and methods of an object
"""


def lookup(obj):
    """ function that returns the list of available attributes
    and methods of an object """
    return (dir(obj))
