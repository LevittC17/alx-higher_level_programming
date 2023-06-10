#!/usr/bin/python3

""" Function that returns an element from a list like in C
If element is negative (less than 0) -> return None
If element is out of range (greater than the length of the list)
-> return None
"""


def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    else:
        return my_list[idx]
