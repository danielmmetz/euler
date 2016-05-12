"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

from prime import isprime
from itertools import permutations
from functools import reduce


def tuple_to_int(t):
    return reduce(lambda x, y: x*10+y, t)


def answer():
    # observation: cannot be 8 or 9 due to divisibility by 3
    for n in range(7, 0, -1):
        possibilities = map(tuple_to_int, permutations(range(n, 0, -1)))
        for candidate in possibilities:
            if isprime(candidate):
                return candidate


if __name__ == '__main__':
    print(answer())

