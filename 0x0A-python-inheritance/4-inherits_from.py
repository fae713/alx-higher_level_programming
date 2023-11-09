#!/usr/bin/python3
"""
This is a module container of the function 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
        inherits_from - if the object is an instance of a class
        that inherited (directly or indirectly) from the specified
        class

        Args:
            obj: initial object
            a_class: the specified class

        Returns: True if the object is an instance of a
                class that inherited from class else False
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
