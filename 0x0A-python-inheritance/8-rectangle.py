#!/usr/bin/python3
""" 8-rectangle module declaration for Rectangle class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle - a class that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ The init method

            Args:
                width: private width attribute
                height: private height attribute

            Returns:
                None
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
