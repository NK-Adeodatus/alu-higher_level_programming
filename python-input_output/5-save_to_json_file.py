#!/usr/bin/python3
"""
Function that writes an object to a text file
using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """Writing a Python object to a file usin json representation"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
