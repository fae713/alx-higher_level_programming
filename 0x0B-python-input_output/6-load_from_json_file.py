#!/usr/bin/python3
""" 6-load_from_json_file module declaration"""
import json


def load_from_json_file(filename):
    """load_from_json_file - A function that creates an Object
        from a “JSON file”

        Args:
            filename (str): The file name to be opened

        Returns:
            A new object
    """

    with open(filename) as f:
        return json.load(f)
