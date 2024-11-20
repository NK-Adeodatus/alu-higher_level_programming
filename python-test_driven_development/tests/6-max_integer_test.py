#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        """Test with a list of both positive and negative numbers"""
        self.assertEqual(max_integer([-1, 0, 2, -4, 3]), 3)

    def test_duplicate_max(self):
        """Test with a list where the max value occurs multiple times"""
        self.assertEqual(max_integer([3, 1, 3, 2]), 3)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 2.2]), 3.3)

    def test_mixed_floats_integers(self):
        """Test with a list of floats and integers"""
        self.assertEqual(max_integer([1.1, 2, 3.3, 2]), 3.3)

    def test_string_characters(self):
        """Test with a list of single character strings"""
        self.assertEqual(max_integer(['a', 'z', 'b']), 'z')

    def test_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_none(self):
        """Test with None as input"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        """Test with a list containing mixed types"""
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

    def test_large_numbers(self):
        """Test with a list of very large integers"""
        self.assertEqual(max_integer([10**10, 10**11, 10**12]), 10**12)


if __name__ == "__main__":
    unittest.main()
