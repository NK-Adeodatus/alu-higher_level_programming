#!/usr/bin/python3
"""
Defines if an object is an instance of
a subclass of a certain class
"""


def inherits_from(obj, a_class):
    """Returns true if obj is an instance of a subclass of a_class"""
    return isinstance(obj, a_class) and type(obj) != a_class
