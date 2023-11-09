#!/usr/bin/python3
""" The 2-is_same_class.py module """


def is_same_class(obj, a_class):
    """ is_same_class: A function that checks
        the object is exactly an instance of the specified class

        Args:
            obj: the object instance
            a_class: the specified class

        Returns:
            True if is an instance
            else False
    """
    if (type(obj) == a_class):
        return (True)
    else:
        return (False)
