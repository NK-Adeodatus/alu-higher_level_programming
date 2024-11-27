#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_no_id(self):
        """Test automatic ID assignment when no id is provided."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_provided_id(self):
        """Test manual ID assignment."""
        b1 = Base(42)
        self.assertEqual(b1.id, 42)

    def test_mixed_ids(self):
        """Test a mix of manual and automatic ID assignments."""
        b1 = Base()
        b2 = Base(99)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 99)
        self.assertEqual(b3.id, 2)

    def test_nb_objects_private(self):
        """Test that __nb_objects is private."""
        with self.assertRaises(AttributeError):
        print(Base.__nb_objects)

    def test_nb_objects_increment(self):
        """Test that __nb_objects increments correctly."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_nb_objects_no_change_with_manual_id(self):
        """Test that providing an id does not increment __nb_objects."""
        b1 = Base()
        b2 = Base(10)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 10)
        self.assertEqual(b3.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)


if __name__ == "__main__":
        unittest.main()
