#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for i in range(len(sys.argv)):
        if (i == 0):
            continue
        else:
            sum += int(sys.argv[i])
    print("{}".format(sum))
