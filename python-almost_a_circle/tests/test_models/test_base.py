#!/usr/bin/env python3
"""
Unit tests for the Base class in models.base.

This module contains tests for various methods in the Base class,
such as JSON serialization/deserialization, file operations, instance
creation, and CSV handling.
"""


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def setUp(self):
        """Set up test environment by resetting Base object count."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up any files created during the tests."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

    def test_to_json_string(self):
        """Test the to_json_string method."""
        dict_list = [{"id": 1, "width": 10, "height": 7}]
        json_string = Base.to_json_string(dict_list)
        self.assertEqual(json_string, '[{"id": 1, "width": 10, "height": 7}]')

        empty_list = []
        self.assertEqual(Base.to_json_string(empty_list), "[]")

        none_list = None
        self.assertEqual(Base.to_json_string(none_list), "[]")

        empty_string = ""
        self.assertEqual(Base.from_json_string(empty_string), [])

        none_string = None
        self.assertEqual(Base.from_json_string(none_string), [])

    def test_save_to_file(self):
        """Test the save_to_file method."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertIn('"id": 1', content)
        self.assertIn('"width": 10', content)

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_load_from_file(self):
        """Test the load_from_file method."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertTrue(isinstance(rectangles[0], Rectangle))
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[1].height, 4)

        squares = Square.load_from_file()
        self.assertEqual(squares, [])

    def test_create(self):
        """Test the create method."""
        rect_dict = {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}
        r1 = Rectangle.create(**rect_dict)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 7)

        square_dict = {"id": 1, "size": 5, "x": 0, "y": 0}
        s1 = Square.create(**square_dict)
        self.assertEqual(s1.size, 5)

    def test_save_to_file_csv(self):
        """Test the save_to_file_csv method."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            content = file.readlines()
        self.assertIn("1,10,7,2,8\n", content)
        self.assertIn("2,2,4,0,0\n", content)

    def test_load_from_file_csv(self):
        """Test the load_from_file_csv method."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file_csv([r1, r2])
        rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[1].height, 4)

        squares = Square.load_from_file_csv()
        self.assertEqual(squares, [])


if __name__ == "__main__":
        unittest.main()
