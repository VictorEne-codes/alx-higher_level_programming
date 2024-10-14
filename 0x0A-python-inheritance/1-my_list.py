#!/usr/bin/python3
"""functiin that prints the list"""


class MyList(list):
    """prints an inherited list"""

    def print_sorted(self):
        """prints sorted list in ascending krder"""
        list_ = self[:]
        list_.sort()
        print(list_)
