#!/usr/bin/python3
"""Defines a Rectangle class with width, height, area, and perimeter."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialzing the rectangle with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieving the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculating the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculating the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
