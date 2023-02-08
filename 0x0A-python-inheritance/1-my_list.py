#!/usr/bin/python3
"""
The program sorts a list
"""


class MyList(list):
    """ clas hat inherits from list """
    def print_sorted(self):
        """ prints the list sorted in ascending order """
        new_list = self[:]
        new_list.sort()
        print(new_list)



