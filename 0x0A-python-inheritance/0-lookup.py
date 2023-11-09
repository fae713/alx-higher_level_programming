#!/usr/bin/python3
""" lookup(obj): A module that conatins a function that
    returns the list of available attributes and methods of
    an object.
"""


def lookup(obj):
    """ The look up method

        Args:
            obj: An object of any data type
        Returns:
            list: A list of methods and attributes of an object
    """
    return (dir(obj))
