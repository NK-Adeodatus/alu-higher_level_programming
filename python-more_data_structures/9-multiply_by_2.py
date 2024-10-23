#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2."""
    keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())
    new_dict = dict(zip(keys, map(lambda x: x * 2, values)))
    return new_dict
