#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set."""
    return {element for element in set_1 if element not in set_2}.union(
           {element for element in set_2 if element not in set_1})
