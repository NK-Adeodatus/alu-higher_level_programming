#!/usr/bin/python3
"""
Defines Student class base on 9-student.py
"""


class Student:
    """Class that contain a method `to_json` that allows filtering
    attributes for JSON serialization."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student object with first name, last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student instance for
        JSON serialization.
        """
        if attrs is None:
            return vars(self)
        
        attrs_dict = {
            key: value
            for key, value in vars(self).items()
            if key in attrs
        }
        return attrs_dict
