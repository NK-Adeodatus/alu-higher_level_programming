#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, a special type of Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (both width and height).
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The identity of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
    """Set the size of the square."""
    self.width = value
    self.height = value
