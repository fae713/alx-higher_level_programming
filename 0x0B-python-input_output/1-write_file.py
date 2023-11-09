#!/usr/bin/python3
""" 1-write_file.py Module Declaration """


def write_file(filename="", text=""):
    """ write_file - a function that writes strings to a file

        Args:
            filename: The file name
            text: the string text to be written

        Returns:
            Integer: The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
