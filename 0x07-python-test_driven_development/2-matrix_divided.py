#!/usr/bin/python3
"""
Matrix division: Returns a new matrix that is
divided using the div value to divide each element
of the matrix.
"""


def matrix_divided(matrix, div):
    """
    divide all elements of a matrix
    """
    s = "matrix must be a matrix (list of lists) of integers or floats"
    if not (matrix or isinstance(matrix, list)):
        raise TypeError(s)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if (len(row) == 0):
            raise TypeError(s)
        if (len(row) != len(matrux[0])):
            raise TypeError("Each row of the matrix must have the same size")
        if not (row or isinstance(row, list)):
            raise TypeError(s)
        for col in row:
            if not (isinstance(col, int) or isinstance(col, float)):
                raise TypeError(s)
        new_matrix = [[round((col / div), 2) for col in row] for row in matrix]
        return (new_matrix)
