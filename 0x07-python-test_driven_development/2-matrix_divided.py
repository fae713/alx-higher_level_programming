#!/usr/bin/python3
""" The 2-matrix_divided Module """


def matrix_divided(matrix, div):
    """
        def matrix_divided(matrix, div)

        Args:
            matrix: a list of lists of integers or floats
            div: a number (integer or float)

        Returns:
            a new matrix
    """
    length = 0
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(err_msg)

    for block in matrix:    # matrix is a list
        if type(block) is not list:
            raise TypeError(err_msg)

        for element in block:
            if type(element) is not int and type(element) is not float:
                raise TypeError(err_msg)

        if len(block) != length and length != 0:
            raise TypeError("Each row of the matrix must have the same size")
        length = len(block)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
