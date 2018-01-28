#!/usr/bin/env python3


def main():
    methods = {
        '-': lambda x, y: x - y,
        '+': lambda x, y: x + y,
        '/': lambda x, y: x / y,
        '*': lambda x, y: x * y,
        'mod': lambda x, y: x % y,
        'pow': lambda x, y: x ** y,
        'div': lambda x, y: x // y,
    }

    first_number = int(input())
    second_number = int(input())
    method = input().lower().strip()

    print(methods[method](first_number, second_number))


if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyError:
            print('Error: unknown operation')

        except (ValueError, TypeError):
            print('Error: enter the 2 float number and operation name')

        except ZeroDivisionError:
            print('Error: zero division')

        except EOFError:
            break
