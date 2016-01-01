"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.
"""

from fractions import Fraction
from operator import mul
from itertools import imap


def reductions(numerator, denominator):
    if numerator[0] == denominator[0] and denominator[1] != '0':
        yield Fraction(int(numerator[1]), int(denominator[1]))
    if numerator[0] == denominator[1] and denominator[1] != '0':
        yield Fraction(int(numerator[1]), int(denominator[0]))
    if numerator[1] == denominator[0] and denominator[1] != '0':
        yield Fraction(int(numerator[0]), int(denominator[1]))
    if numerator[1] == denominator[1] != '0':
        yield Fraction(int(numerator[0]), int(denominator[0]))


def answer():
    non_trivials = []
    for denominator in imap(str, xrange(10, 100)):
        for numerator in imap(str, xrange(10, int(denominator))):
            for reduced in reductions(numerator, denominator):
                if reduced == Fraction(int(numerator), int(denominator)):
                    non_trivials.append(reduced)
    return reduce(mul, non_trivials).denominator


if __name__ == '__main__':
    print answer()
