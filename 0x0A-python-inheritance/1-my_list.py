#!/usr/bin/python3
""" The MyList Module """


class MyList(list):
    """ My List class that derives from the
        in-built python list class
    """

    def __init__(self):
        """ The init function declarartion """
        super().__init__()

    def print_sorted(self):
        """ The print sorted method

            Args:
                self: this reference

            Returns:
                list: a reverse sorted list
        """
        print(sorted(self))
