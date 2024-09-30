#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(int(my_list[i])), end="")
        print()
    except IndexError:
        print("out of range")
    except ValueError:
        print("not converted")
    except TypeError:
        print("Not an integer")
