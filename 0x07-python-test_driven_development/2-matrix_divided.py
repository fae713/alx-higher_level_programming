#!/usr/bin/python3
""" The 2-matrix_divided module"""


def matrix_divided(matrix, div):
    """This defines function that divides all elements
    of a matrix.

    Args:
        matrix: a list of matrix that's either an integer or a float
        div: a number (integer or float)

    returns:
        Divided elements of a matrix """

    error_msg = "matrix must be a matrix(list of list) of integers/floats"
    lenght = 0

    if type(matrix) is not list:
        raise TypeError(error_msg)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)

        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError(error_msg)

        if len(row) != length and length != 0:
            raise TypeError("Each row of the matrix must have the same size")
        length = len(row)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in row] for row in matrix]
