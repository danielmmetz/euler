"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from itertools import combinations


def answer(n_digits):
    """
    finds the largest palindrome made from the project of two numbers, each
    composed of n_digits
    """

    best = 0
    pairs = combinations(xrange(10 ** (n_digits - 1), 10 ** (n_digits)), 2)

    for (x, y) in pairs:
        prod = str(x * y)
        if prod == prod[::-1]:
            best = max(best, x * y)

    return best


if __name__ == '__main__':
    assert answer(2) == 9009, 'failed small test'
    print answer(3)
