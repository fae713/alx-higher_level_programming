#!/usr/bin/python3
""" This module returns the peak of the list
"""


def find_peak(list_of_integers):
    """ This function returns the peak of the list
    """
    if not list_of_integers:
        return None
    start = 0
    end = len(list_of_integers)
    middle = ((end - start) // 2) + start
    middle = int(middle)
    if end == 1:
        return list_of_integers[0]
    if end == 2:
        return max(list_of_integers)
    if list_of_integers[middle] >= list_of_integers[middle - 1] and\
            list_of_integers[middle] >= list_of_integers[middle + 1]:
        return list_of_integers[middle]
    if middle > 0 and list_of_integers[middle] < list_of_integers[middle + 1]:
        return find_peak(list_of_integers[middle:])
    if middle > 0 and list_of_integers[middle] < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])
