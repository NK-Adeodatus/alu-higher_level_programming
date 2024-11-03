#!/usr/bin/python3
"""A function for checking if obj is instance
of a class or the subclass of a_class"""


def is_kind_of_class(obj, a_class):
    """Return true if obj is instance of a_class
    or it's subclass"""
    return instance(obj, a_class)
