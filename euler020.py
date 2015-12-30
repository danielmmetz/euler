# coding=utf8

"""
n! means n * (n − 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import operator


def factorial(n):
    return reduce(operator.mul, xrange(1, n+1))


def answer(n):
    return sum(int(digit) for digit in str(factorial(n)))


if __name__ == '__main__':
        print answer(100)