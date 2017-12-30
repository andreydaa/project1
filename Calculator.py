#!/usr/bin/env python3

methods = {
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    'mod': lambda x, y: x % y,
    'pow': lambda x, y: x ** y,
    'div': lambda x, y: x // y,
}

while True:
    try:
        first_number = int(input())
        second_number = int(input())
        method = input().lower()

        print(methods[method](first_number, second_number))

    except KeyError:
        print('Error: unknown operation')

    except (ValueError, TypeError):
        print('Error: enter the 2 float number and operation name')

    except ZeroDivisionError:
        print('Error: zero division')

    except EOFError:
        break
