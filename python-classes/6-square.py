#!/usr/bin/python3
"""Module 6-square - Defines a square with size and position properties."""


class Square:
    """Class that defines a square with size and position properties."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with an optional size and position."""
        self.size = size  # Use the setter to initialize size
        self.position = position  # Use the setter to initialize position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with type checks."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with character '#' considering the position."""
        if self.__size == 0:
            print("")  # Print an empty line if size is 0
            return

        # Print the position (spaces) before the square
        for _ in range(self.__position[1]):
            print("")  # Print new lines for vertical position

        for _ in range(self.__size):
            print(" " * self.__position[0] + '#' * self.__size)
