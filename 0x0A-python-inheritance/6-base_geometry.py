#!/usr/bin/python3
""" Empty Geometry class """


class BaseGeometry:
    """ class that improves geometry """
    def area(self):
        """ raises exception with message area() not implemented """
        raise Exception("area() is not implemented")
