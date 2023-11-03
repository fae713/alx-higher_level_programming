#!/usr/bin/python3
""" This defines a text indentation Module"""


def text_indentation(text):
    """
    prints a text with 2 new lines after (, . ? and :)

    Args:
        text: the string to work on"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    fae = False
    for i in range(len(text)):
        if fae and text[i] == ' ':
            continue
        else:
            print(text[i], end="")
            fae = False
        if text[i] in ['.', '?', ':']:
            print()
            print()
            fae = True
