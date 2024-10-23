#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """Replace an element at a specific position in the list.

    If idx is negative or out of range, return the original list.
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
