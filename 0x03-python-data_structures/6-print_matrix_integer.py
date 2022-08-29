#!/usr/bin/python3

# use a loop to iterate the main list
# use another loop to iterate the lists in the main list
# print out the element in the inner loop
# increment to access the next element of the main list
# print out elements

def print_matrix_integer(matrix=[[]]):
    """print matrix
    """

    for i in matrix:
        print(' '.join(["{:d}".format(x) for x in i]))
