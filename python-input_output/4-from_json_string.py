#!/usr/bin/python3
"""Function to convert json strin to python object"""


import json


def from_json_string(my_str):
    """Converting a json file to a Python object"""
    return json.loads(my_str)
