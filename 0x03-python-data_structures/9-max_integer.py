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

    if len(my_list) < 0:
        return None

    biggest_int = my_list[0]

    for i in range(1, len(my_list) - 1):
        if biggest_int < my_list[i]:
            biggest_int = my_list[i]
        else:
            continue
        i += 1

    return biggest_int
