#!/usr/bin/python3
"""
Defines a class Rectangle that inherits
from BaseGeometry.
"""


class Rectangle(BaseGeometry):
    """
    A class to represent rectangle
    using baseGeometry.
    """

    def __init__(self, width, height):
        """Initialize a new rectangle instance."""
        #Validate width and height using integer_validator method
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        #set private attributes for width and height
        self.__width = width
        self.__height =height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
