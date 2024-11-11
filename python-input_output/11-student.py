#!/usr/bin/python3
""" Student class module
"""


class Student:
    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a
        Student instance"""
        if attrs is None:
            return vars(self)
        
        attrs_dict = {
            key: value
            for key, value in vars(self).items()
            if key in attrs
        }
        return attrs_dict

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance
        using json"""
        for key, value in json.items():
            setattr(self, key, value)
