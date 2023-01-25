#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
    if (x > 0):
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end='')
                idx += 1
            except:
                break
    print('')
    return (idx)
