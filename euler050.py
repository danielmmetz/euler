"""
The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-
hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from prime import isprime, prime_list, _refresh
from math import sqrt, log10


def answer(limit=1000000):
    _refresh(limit // pow(10, sqrt(log10(limit))-1))
    for length in range(int(sqrt(limit)), 0, -1):
        for end in range(len(prime_list), length-1, -1):
            candidate = sum(prime_list[end-length:end])
            if candidate < limit and isprime(candidate):
                return candidate


if __name__ == '__main__':
    print(answer())


