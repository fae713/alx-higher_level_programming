#!/usr/bin/python3
""" 2-append_write.py Module Declaration """


def append_write(filename="", text=""):
    """ append_write - a function that appends a string at the
        end of a text file

        Args:
            filename (str): The filename
            text: the string to be appended at the end of the file

        Returns:
            Integer: the number of characters added
    """
    with open(filename, "a") as f:
        return f.write(text)
