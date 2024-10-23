#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds two tuples."""
    a1, a2 = (tuple_a + (0, 0))[:2]  # Default to 0 if missing
    b1, b2 = (tuple_b + (0, 0))[:2]  # Default to 0 if missing
    return (a1 + b1, a2 + b2)
