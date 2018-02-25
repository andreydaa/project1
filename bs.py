#!/usr/bin/env python3
"""
Binary search.
Based on book "Grokking Algorithms".
https://github.com/egonSchiele/grokking_algorithms
"""


def binary_search(lst, value, low, high):
    """binary search method"""
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        slot = lst[mid]
        if slot == value:
            return mid
        elif slot < value:
            low = mid + 1
        else:
            high = mid - 1
    return binary_search(lst, value, low, high)
