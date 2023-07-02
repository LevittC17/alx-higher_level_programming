#!/usr/bin/python3

"""
Find peak in a list of unsorted integers
There might be more than one peak in the list
"""


def find_peak(list_of_integers):
    """
    Returns a peak in a list of unsorted integers.
    Args: list_of_integers (list): unsorted
    Return:peak element in the list, or None if empty.
    """

    if not list_of_integers:  # Check if the list is empty
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Check if the middle element is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # Search in the left half
            right = mid
        else:
            # Search in the right half
            left = mid + 1

    return list_of_integers[left]
