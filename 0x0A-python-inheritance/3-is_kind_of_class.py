#!/usr/bin/python3
""" The 3-is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class: method that checks
        if the object is an instance of a class
        that derives from the specified class

        Args:
            obj: An object instance
            a_class: The specified class

        Returns:
            True if it is an instance
            else False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
