"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from itertools import chain, count
from prime import isprime, prime


def is_truncatable_prime(n):
    n_str = str(n)
    if len(n_str) == 1: return False
    leftwise  = [int(n_str[:i]) for i in range(1, len(n_str))]
    rightwise = [int(n_str[i:]) for i in range(len(n_str))]
    return all(isprime(i) for i in chain(leftwise, rightwise))


def answer(limit=11):
    hits, total = 0, 0
    for pos in count():
        if is_truncatable_prime(prime(pos)):
            hits += 1
            total += prime(pos)
        if hits == limit:
            return total


if __name__ == '__main__':
    print(answer())