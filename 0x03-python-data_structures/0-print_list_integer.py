#!/usr/bin/python3
"""
A function that prints all integers of a list
Format: One integer per line, no module imported
"""

def print_list_integer(my_list=[]):
    for i in my_list:
        # Format one integer per line
        print("{:d}".format(i))
