#!/usr/bin/python3
"""Module 4-square - Defines a square with
size property and area calculation."""


class Square:
    """Class that defines a square with a size property."""

    def __init__(self, size=0):
        """Initialize the square with an optional size."""
        self.size = size  # Use the setter to initialize size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
