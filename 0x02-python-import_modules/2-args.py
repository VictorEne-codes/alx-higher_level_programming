#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ac = len(sys.argv) - 1
    if ac == 1:
        print("{} argument:".format(ac))
    elif ac == 0:
        print("{} arguments.".format(ac))
    else:
        print("{} arguments:".format(ac))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
