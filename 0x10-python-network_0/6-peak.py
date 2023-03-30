def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    mid = n // 2
    if (mid == n - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]) and \
            (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]):
        return list_of_integers[mid]
    elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
