#!/usr/bin/python3
"""Unit tests for the Rectangle class."""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Set up test objects before each test."""
        self.rect1 = Rectangle(3, 4)
        self.rect2 = Rectangle(5, 6, 2, 3, 10)

    def tearDown(self):
        """Clean up after tests."""
        del self.rect1
        del self.rect2

    def test_initialization(self):
        """Test proper initialization of Rectangle instances."""
        self.assertEqual(self.rect1.width, 3)
        self.assertEqual(self.rect1.height, 4)
        self.assertEqual(self.rect1.x, 0)
        self.assertEqual(self.rect1.y, 0)
        self.assertIsNotNone(self.rect1.id)

        self.assertEqual(self.rect2.width, 5)
        self.assertEqual(self.rect2.height, 6)
        self.assertEqual(self.rect2.x, 2)
        self.assertEqual(self.rect2.y, 3)
        self.assertEqual(self.rect2.id, 10)

    def test_width_setter_and_getter(self):
        """Test width property."""
        self.rect1.width = 10
        self.assertEqual(self.rect1.width, 10)
        with self.assertRaises(TypeError):
            self.rect1.width = "10"
        with self.assertRaises(ValueError):
            self.rect1.width = -1

    def test_height_setter_and_getter(self):
        """Test height property."""
        self.rect1.height = 15
        self.assertEqual(self.rect1.height, 15)
        with self.assertRaises(TypeError):
            self.rect1.height = [10]
        with self.assertRaises(ValueError):
            self.rect1.height = 0

    def test_x_setter_and_getter(self):
        """Test x property."""
        self.rect1.x = 3
        self.assertEqual(self.rect1.x, 3)
        with self.assertRaises(TypeError):
            self.rect1.x = None
        with self.assertRaises(ValueError):
            self.rect1.x = -5

    def test_y_setter_and_getter(self):
        """Test y property."""
        self.rect1.y = 7
        self.assertEqual(self.rect1.y, 7)
        with self.assertRaises(TypeError):
            self.rect1.y = 5.5
        with self.assertRaises(ValueError):
            self.rect1.y = -3

    def test_area(self):
        """Test the area method."""
        self.assertEqual(self.rect1.area(), 12)
        self.assertEqual(self.rect2.area(), 30)

    def test_update_args(self):
        """Test the update method with *args."""
        self.rect1.update(20, 8, 9, 1, 2)
        self.assertEqual(self.rect1.id, 20)
        self.assertEqual(self.rect1.width, 8)
        self.assertEqual(self.rect1.height, 9)
        self.assertEqual(self.rect1.x, 1)
        self.assertEqual(self.rect1.y, 2)

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        self.rect2.update(width=10, height=15, y=4)
        self.assertEqual(self.rect2.width, 10)
        self.assertEqual(self.rect2.height, 15)
        self.assertEqual(self.rect2.y, 4)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        rect_dict = self.rect1.to_dictionary()
        self.assertEqual(rect_dict["width"], 3)
        self.assertEqual(rect_dict["height"], 4)
        self.assertEqual(rect_dict["x"], 0)
        self.assertEqual(rect_dict["y"], 0)
        self.assertIsNotNone(rect_dict["id"])

    def test_str_representation(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.rect1), "[Rectangle] ({}) 0/0 - 3/4".format(self.rect1.id))
        self.assertEqual(str(self.rect2), "[Rectangle] (10) 2/3 - 5/6")


if __name__ == "__main__":
        unittest.main()
