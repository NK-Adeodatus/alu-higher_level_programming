#!/usr/bin/python3
"""Creating an object from a json file"""


import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file"""
    with open(filename, 'r') as file:
        return json.load(file)
