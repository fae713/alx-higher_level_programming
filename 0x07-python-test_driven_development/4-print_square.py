#!/usr/bin/python3
""" This is a square printing Module """


def print_square(size):
    """
    prints a square with the character '#'

    Args:
        size: size is the lenght of the square"""

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        for b in range(size):
            print("#", end='')
        print()
