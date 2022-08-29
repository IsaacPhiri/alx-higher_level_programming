#!/usr/bin/python3

# if a tuple is smaller than 2, then use value 0
# if tuple is bigger than 2, use only the first 2 int

# if tuple_a and tuple_a, then tuple_a + tuple_b

def add_tuple(tuple_a=(), tuple_b=()):

    a = len(tuple_a)
    b = len(tuple_b)

    new_tup = ((tuple_a[0] if a >= 1 else 0) + (tuple_b[0] if b >= 1 else 0),
               (tuple_a[1] if a >= 2 else 0) + (tuple_b[1] if b >= 2 else 0))
    return new_tup
