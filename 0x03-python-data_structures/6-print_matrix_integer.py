#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        j = ""
        for k in i:
            print("{:j}{:d}".format(j, k), end='')
            j = " "
        print()
