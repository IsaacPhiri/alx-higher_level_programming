#!/usr/bin/python3

# function that returns a tuple with the length of a\
# string and its first character.

# check if string is empty, if empty then string is equal to None
# if string is not empty then return its length and the first letter.

def multiple_returns(sentence):
    """Check string and return length
    and first letter.
    """
    
    if len(sentence) == 0:
        sentence = None
        return

    check_len = len(sentence), sentence[0]

    return check_len
