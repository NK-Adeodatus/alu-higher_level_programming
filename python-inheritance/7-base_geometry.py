#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """An empty class."""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value"""
        if isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
