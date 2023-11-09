#!/usr/bin/python3
""" append_after module declaration
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.

    """

    words = ""

    with open(filename, "r") as f:
        for line in f:
            words += line
            if line.find(search_string) != -1:
                words += new_string

    with open(filename, "w") as w:
        w.write(words)
