#!/usr/bin/env python3
"""Binary search module"""

from bs import binary_search


def main():
    
    """main function"""
    lst = [int(i) for i in input().split()]
    lst.sort()
    value = int(input())
    low = 0
    high = len(lst) - 1

    print(binary_search(lst, value, low, high))


if __name__ == '__main__':
    main()
