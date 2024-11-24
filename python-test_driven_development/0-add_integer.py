#!/usr/bin/python3
"""
Module to add two integers
"""


def add_integer(a, b=98):
    """
        Add two integers or floats.

        >>> add_integer(1, 2)
        3
        >>> add_integer(100.3, -2)
        98
        >>> add_integer("hello", 5)
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
