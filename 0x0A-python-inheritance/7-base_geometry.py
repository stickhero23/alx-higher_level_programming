#!/usr/bin/python3
""" Module 7-base_geometry """


class BaseGeometry:
    """
    Methods:
        area(self)
        integer_validator(self, name, value)
    improves the geometry with validator 
    """
    def area(self):
        """ not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates input """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
  

