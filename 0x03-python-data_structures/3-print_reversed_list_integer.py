#!/usr/bin/python3

# create a var to hold the reversed string
# use a for loop to print out the elements of the reversed list

def print_reversed_list_integer(my_list=[]):
    """Reversed list
    """

    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
