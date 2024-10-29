#!/usr/bin/python3
"""Module 1-square Defines a square based on module 0-square."""


class Square:
    """Empty class that defines a square"""
    def __init__(self, size=0):
        """Instantiate with size duriing object initialization"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculate and return the area of a square."""
        return self.__size ** 2
