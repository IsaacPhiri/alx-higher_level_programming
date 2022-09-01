#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """a function that computes the square
    value of all integers of a matrix.
    """

    square = [list(map((lambda x: x**2), elements)) for elements in matrix]
    return square
