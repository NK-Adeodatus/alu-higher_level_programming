#!/usr/bin/python3
"""Defines a base class."""
import json
import csv
import turtle


class Base:
    """Represent the base model.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        # If list_objs is None, save an empty list
        if list_objs is None:
            list_objs = []

        list_dicts = [obj.to_dictionary() for obj in list_objs]

        # Get the class name and form the filename
        filename = f"{cls.__name__}.json"

        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @classmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            from models.rectangle import Rectangle
            new_instance = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            from models.square import Square
            new_instance = Square(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dictionaries = cls.from_json_string(json_string)
                instances = []
                for dictionary in list_dictionaries:
                    instances.append(cls.create(**dictionary))
                    return instances

        except FileNotFoundError:
            return []
