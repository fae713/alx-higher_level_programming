#!/usr/bin/python3
""" 4-from_json_string.py  module """
import json


def from_json_string(my_str):
    """ from_json_string - A function that deserializes json data
        into python objects

        Args:
            my_str: json string

        Returns:
            Python data structure (objects)
    """
    return json.loads(my_str)
