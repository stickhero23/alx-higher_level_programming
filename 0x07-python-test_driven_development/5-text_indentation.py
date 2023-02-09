#!/usr/bin/python3
"""
Module 5-text_indentation
Prints a text with 2 new lines after ., ?, and :
"""
def text_indentation(text):
    """
    Prints text with 2 new lines after ".", "?", and ":"
    """
    if (type(text) is not str or ext is None):
        raise TypeError("text must be a string")
    flag = 0
    for c in text:
        if (c == '.' or c == '?' or c == ':'):
            print(c, end='')
            print('')
            print('')
            flag = 1
        else:
            if (flag == 0):
                print(c, end='')
            else:
                if (c == ' ' or c == '\t'):
                    pass
                else:
                    print(c, end="")
                    flag = 0

