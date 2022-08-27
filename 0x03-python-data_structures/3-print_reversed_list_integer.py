#!/usr/bin/python3

# create a var to hold the reversed string
# use a for loop to print out the elements of the reversed list

def print_reversed_list_integer(my_list=[]):
    """Reversed list
    """

    rev_list = my_list[::-1]
    for i in range(0, len(rev_list)):
        print("{:d}".format(rev_list[i]))
