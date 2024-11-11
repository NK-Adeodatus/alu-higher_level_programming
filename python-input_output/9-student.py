#!/usr/bin/python3
"""
This module contains the Student class, which defines
a student with first name, last name, and age.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes the student object with first name, last name,
        and age.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the student instance
        for JSON serialization.
        """
        return vars(self)
