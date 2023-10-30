#!/usr/bin/python3
"""This is the sqaure module"""


class Square:
    """This class defines a sqaure instance"""

    def __init__(self, size=0):
        """This method defines the sqaure object"""

        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """This describes an Area of a square"""

        return self.__size ** 2
