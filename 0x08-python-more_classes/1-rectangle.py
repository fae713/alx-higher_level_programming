#!/usr/bin/python3
"""This defines a class called Rectangle"""


class Rectangle:
    """This is a Rectangle Class"""

    def __init__(self, width=0, height=0):
        """Init is the initialization method"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter property of Width"""
        return self.__width

    @property
    def height(self):
        """The getter property of Height"""

        return self.__height

    @width.setter
    def width(self, value):
        """The setter property of width"""

        if type(value) is not int:
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("Width must be >=0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """The setter property of height"""

        if type(value) is not int:
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("Height must be >=0")
        else:
            self.__height = value
