#!/usr/bin/python3
""" The 0-read_file module declaration """


def read_file(filename=""):
    """ read_file - read a file and print its content

        Args:
            filename (str): A string describing the filename

        Returns:
            None
    """

    with open(filename, "r") as f:
        for line in f:
            print(line, end="")
