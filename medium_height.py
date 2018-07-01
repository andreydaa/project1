#!/usr/bin/env python3

from collections import OrderedDict


def main():
    
    results = OrderedDict({i: [] for i in range(1, 12)})

    with open('example.txt', 'r') as f:
        for line in f:
            value = line.split()
            results[int(value[0])].append(int(value[2]))

    for key, value in results.items():
        value = sum(value) / len(value) if value != [] else '-'
        print('{} {:.2f}'.format(key, value))


if __name__ == '__main__':
    main()
