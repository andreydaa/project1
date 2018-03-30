#!/usr/bin/env python3

GLOBAL = 'global'


def get(namespaces, name, var):
    if var in namespaces[name]['variables']:
        return name
    elif name == GLOBAL:
        return None
    else:
        return get(namespaces, namespaces[name]['parents'], var)


def main():
    count = int(input())
    namespaces = {GLOBAL: {'parents': None, 'variables': []}}
    for _ in range(count):
        command, name, var = input().split()
        if command == 'add':
            namespaces[name]['variables'].append(var)
        elif command == 'create':
            namespaces[name] = {'parents': var, 'variables': []}
        else:
            print(get(namespaces, name, var))


if __name__ == '__main__':
    main()
