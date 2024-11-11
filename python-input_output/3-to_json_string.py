#!/usr/bin/python3
"""Returning the json representation of an object"""


import json


def to_json_string(my_obj):
    """Turning an object in a json string"""
    return json.dumps(my_obj)
