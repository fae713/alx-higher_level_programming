#!/usr/bin/python3
"""This defines a class"""


class Rectangle:
    """This is a representation of a rectangle class"""
    def __init__(self, width=0, height=0):
        """This is an initialization method of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """This is the getter for private instance attribute of width"""
        return self.__width

    @property
    def height(self):
        """This is the getter for private instance attribute of height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter for the private instance of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >-= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Setter for the private instance of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """This returns the area  of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """This returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation of the rectangle for
        recreation of a new instance"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
