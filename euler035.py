"""
The number, 197, is called a circular prime because all rotations of the digits:
    197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from itertools import cycle
from prime import isprime, prime_list, _refresh


def rotations(num):
    digits = [int(digit) for digit in str(num)]
    n_digits = len(digits)
    circle = [d for (_, d) in zip(range(2*n_digits), cycle(digits))]
    candidates = []
    for start in range(1, n_digits):
        candidate = circle[start:start+n_digits]
        candidate = int(''.join(map(str, candidate)))
        candidates.append(candidate)
    return candidates


def answer(limit=1000000):
    global prime_list
    _refresh(limit)

    count = 0
    for candidate in prime_list:
        if all(map(isprime, rotations(candidate))):
            count += 1
    return count


if __name__ == '__main__':
    print(answer(1000000))


