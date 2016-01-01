# encoding=utf8
"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

from math import log
from itertools import permutations

def perm_to_num(perm):
    num = 0
    for digit in perm:
        num *= 10
        num += digit
    return num


def answer(digits):
    valid_products = set()

    max_multiplicand_len = len(digits)/2 + 1
    for perm in permutations(digits):
        for multiplicand_digits in xrange(1, max_multiplicand_len):
            max_multiplier_pos = len(digits) - len(digits)/2 + 1
            for multiplier_end in xrange(multiplicand_digits, max_multiplier_pos):
                multiplicand = perm_to_num(perm[:multiplicand_digits])
                multiplier = perm_to_num(perm[multiplicand_digits:multiplier_end])
                product = perm_to_num(perm[multiplier_end:])
                if multiplicand*multiplier == product:
                    valid_products.add(product)

    return sum(valid_products)


if __name__ == '__main__':
    print answer(range(1, 10))

