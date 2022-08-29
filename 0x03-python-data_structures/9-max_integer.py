#!/usr/bin/python3

# a function that finds the biggest int of a list

# check if the list is empty, if empty return None
# using a loop, iterate the list to check the items
# store the first element as the biggest int
# using indexes, compare the first element to the second
# if the second element is bigger then it becomes the biggest
# else compare the first to the third
# when through return the biggest int

def max_integer(my_list=[]):
    """a function to find the biggest
    int in a list.
    """

    if my_list:
        my_list.sort()
        biggest = my_list[-1]
        return biggest
    else:
        return None
