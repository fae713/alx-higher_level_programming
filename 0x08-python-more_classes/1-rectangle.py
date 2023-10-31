#!/usr/bin/python3
"""Define a class called Rectangle"""


class Rectangle:
    """This is a Rectangle Class"""

    def __init__(self, width=0, height=0):
        """Init is the initialization method"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter property of width"""
        return self.__width

    @property
    def height(self):
        """The getter property of height"""

        return self.__height

    @width.setter
    def width(self, value):
        """The setter property of width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """The setter property of height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
