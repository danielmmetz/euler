"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def answer(sumval):
    """ returns the product of a Pythagorean triplet whose sum equals sumval """
    for a in xrange(1, sumval):
        for b in xrange(a, sumval):
            c = sumval - a - b
            if c > 0 and c ** 2 == a ** 2 + b ** 2:
                return a * b * c
    raise Exception, 'no triplet exists'


if __name__ == '__main__':
    print answer(1000)
