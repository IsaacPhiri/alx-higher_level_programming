#!/usr/bin/python3

# If idx is less than zero or idx is out of range,
# Return my-list
# else return my_list[idx] = element

def replace_in_list(my_list, idx, element):
    """Replace element in a list
    """

    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
