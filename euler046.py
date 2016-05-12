"""
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""

from itertools import count
from math import sqrt
from prime import isprime, prime_list


def answer():
    for candidate in count(3, 2):
        if isprime(candidate):
            continue
        for p in prime_list:
            remainder = candidate - p
            root = sqrt(remainder//2)
            if root == int(root):
                break
        else:
            return candidate



if __name__ == '__main__':
    print(answer())
