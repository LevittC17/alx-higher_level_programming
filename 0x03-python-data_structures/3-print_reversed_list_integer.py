#!/usr/bin/python3

"""
Function to print all integers of a list in reverse order
Format: One integer per line
"""


def print_reverse_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(i))
