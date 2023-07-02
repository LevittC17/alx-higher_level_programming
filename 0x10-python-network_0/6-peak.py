#!/usr/bin/python3

"""
Finding a peak in a list of
unsorted integers
"""


def find_peak(list_of_integers):
    # Get the length of the list
    n = len(list_of_integers)

    # Base case: if the list is empty, there is no peak
    if n == 0:
        return None

    # Base case: if the list has only one element, it is a peak
    if n == 1:
        return list_of_integers[0]

    # Base case: if the first element is a peak
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]

    # Base case: if the last element is a peak
    if list_of_integers[n-1] >= list_of_integers[n-2]:
        return list_of_integers[n-1]

    # Perform binary search for a peak
    left = 1
    right = n - 2

    while left <= right:
        mid = (left + right) // 2
        mid_val = list_of_integers[mid]

        # Check if the middle element is a peak
        if list_of_integers[mid-1] <= mid_val >= list_of_integers[mid+1]:
            return mid_val
        elif list_of_integers[mid-1] > mid_val:
            # Search in the left half
            right = mid - 1
        else:
            # Search in the right half
            left = mid + 1

    return None
