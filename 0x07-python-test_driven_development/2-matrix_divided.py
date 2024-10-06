#!/usr/bin/python3
"""Funtion to divide a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.

    Args:
        matrix: list of list of integers or floats.
        div: number that divides matrix.

    Return: A new matrix.

    Raises:
        TypeError: If `matrix` is not a
        matrix (list of lists) of integers/floats.
        TypeError: If `div` is not a number.
        ZeroDivisionError: If `div` is zero.
    """
    row_length = len(matrix[0])
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list\
                    of lists) of integers/floats")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list\
                        of lists) of integers/floats")
        if len(i) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
