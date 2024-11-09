#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class to represent a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """Initialize a new square instance."""
        # Validate size using the integer_validator method from BaseGeometry
        self.integer_validator("size", size)

        # Set private attribute for size
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
