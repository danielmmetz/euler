#! /usr/bin/python3
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from functools import lru_cache, reduce
from operator import mul


@lru_cache(maxsize=10)
def factorial(n):
    if n <= 1:
        return 1
    return reduce(mul, range(1, n+1))


def max_value():
    BIGGEST_DIGIT = 9
    max_contribution = factorial(BIGGEST_DIGIT)
    num_digits = 1
    while num_digits*max_contribution > 10**num_digits:
        num_digits += 1
    return num_digits*factorial(BIGGEST_DIGIT)


def answer():
    valid_nums = []
    for num in range(3, max_value()):
        if sum(map(factorial, map(int, str(num)))) == num:
            valid_nums.append(num)
    return sum(valid_nums)


if __name__ == '__main__':
    print(answer())
