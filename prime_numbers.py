#!/usr/bin/env python3


def primes():
    number = 2
    factorial = 1
    while True:
        factorial *= number - 1
        if not (factorial + 1) % number:
            yield number
        number += 1
