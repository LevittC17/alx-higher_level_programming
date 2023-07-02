#!/usr/bin/python3
def find_peak(list_of_integers):
    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)


def find_peak_recursive(arr, left, right):
    mid = (left + right) // 2

    # Check if mid element is a peak
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and
    (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
        return arr[mid]

    # If the left neighbor is greater, search in the left half
    if mid > 0 and arr[mid - 1] > arr[mid]:
        return find_peak_recursive(arr, left, mid - 1)

    # If the right neighbor is greater, search in the right half
    return find_peak_recursive(arr, mid + 1, right)


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
