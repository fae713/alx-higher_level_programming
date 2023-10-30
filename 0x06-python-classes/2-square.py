#!/usr/bin/python3
"""This runs the python interpreter"""


class Square:
    """This defines a class called Square"""


def __init__(self, size=0):
    """This defines an instance attributes"""

    self.__size = size
    """This is a private instance of the square size"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >=0")
    else:
        self.__size = size
