#!/usr/bin/python3
""" finding a peak in a list of integers"""


def find_peak(list_of_integers):
    """function to find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): a list of integers

    Returns:
        int: peak(s)
    """
    list_int = list_of_integers
    if list_int == []:
        return None
    length_int = len(list_int)

    start, end = 0, length_int - 1
    while start < end:
        mid = start + (end - start) // 2
        if list_int[mid] > list_int[mid - 1] and list_int[mid] > list_int[mid + 1]:
            return list_int[mid]
        if list_int[mid - 1] > list_int[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_int[start]
