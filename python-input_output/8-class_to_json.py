#!/usr/bin/python3
"""
This module contains the function `class_to_json`,
which takes an object
and returns its dictionary representation for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for
    JSON serialization.
    """
    return vars(obj)
