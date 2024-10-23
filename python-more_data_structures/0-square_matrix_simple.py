#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix."""
    new_matrix = []
    for inner in matrix:
        new_row = []
        for elem in inner:
            new_row.append(elem ** 2)
        new_matrix.append(new_row)
    return new_matrix
