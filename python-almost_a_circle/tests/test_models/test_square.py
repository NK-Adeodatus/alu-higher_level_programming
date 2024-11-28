#!/usr/bin/python3
"""Unit tests for the Square class."""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Set up test objects before each test."""
        self.sq1 = Square(5)
        self.sq2 = Square(7, 2, 3, 10)

    def tearDown(self):
        """Clean up after tests."""
        del self.sq1
        del self.sq2

    def test_initialization(self):
        """Test proper initialization of Square instances."""
        self.assertEqual(self.sq1.size, 5)
        self.assertEqual(self.sq1.x, 0)
        self.assertEqual(self.sq1.y, 0)
        self.assertIsNotNone(self.sq1.id)

        self.assertEqual(self.sq2.size, 7)
        self.assertEqual(self.sq2.x, 2)
        self.assertEqual(self.sq2.y, 3)
        self.assertEqual(self.sq2.id, 10)

    def test_size_property(self):
        """Test size getter and setter."""
        self.sq1.size = 8
        self.assertEqual(self.sq1.size, 8)
        self.assertEqual(self.sq1.width, 8)
        self.assertEqual(self.sq1.height, 8)
        with self.assertRaises(TypeError):
            self.sq1.size = "10"
        with self.assertRaises(ValueError):
            self.sq1.size = -5

    def test_x_property(self):
        """Test x coordinate getter and setter."""
        self.sq1.x = 3
        self.assertEqual(self.sq1.x, 3)
        with self.assertRaises(TypeError):
        self.sq1.x = "3"
        with self.assertRaises(ValueError):
        self.sq1.x = -1

    def test_y_property(self):
        """Test y coordinate getter and setter."""
        self.sq1.y = 4
        self.assertEqual(self.sq1.y, 4)
        with self.assertRaises(TypeError):
            self.sq1.y = [4]
        with self.assertRaises(ValueError):
            self.sq1.y = -2

    def test_update_with_args(self):
        """Test the update method with *args."""
        self.sq1.update(20, 10, 5, 6)
        self.assertEqual(self.sq1.id, 20)
        self.assertEqual(self.sq1.size, 10)
        self.assertEqual(self.sq1.x, 5)
        self.assertEqual(self.sq1.y, 6)

    def test_update_with_kwargs(self):
        """Test the update method with **kwargs."""
        self.sq2.update(size=12, x=3, y=1)
        self.assertEqual(self.sq2.size, 12)
        self.assertEqual(self.sq2.x, 3)
        self.assertEqual(self.sq2.y, 1)
        self.assertEqual(self.sq2.id, 10)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        sq_dict = self.sq1.to_dictionary()
        self.assertEqual(sq_dict["id"], self.sq1.id)
        self.assertEqual(sq_dict["size"], self.sq1.size)
        self.assertEqual(sq_dict["x"], self.sq1.x)
        self.assertEqual(sq_dict["y"], self.sq1.y)

    def test_str_representation(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.sq1), "[Rectangle] ({}) 0/0 - 5".format(self.sq1.id))
        self.assertEqual(str(self.sq2), "[Rectangle] (10) 2/3 - 7")


if __name__ == "__main__":
        unittest.main()
