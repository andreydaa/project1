#!/usr/bin/env python3

import json


def total(name, parents, grades, rest):
    for parent in parents:
        rest[parent].add(name)
        total(name, grades[parent], grades, rest)


def main():
    data = json.loads(input())
    grades, rest = {}, {}

    for grade in data:
        grades[grade['name']] = grade['parents']
        rest[grade['name']] = {grade['name']}
    
    for name, parents in grades.items():
        total(name, parents, grades, rest)

    for name, childrens in sorted(rest.items()):
        print('{} : {}'.format(name, len(childrens)))


if __name__ == '__main__':
    main()
