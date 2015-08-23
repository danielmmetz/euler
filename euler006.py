"""
The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def answer(seqmax):
    """
    returns the difference between the sum of squares of the first seqmax
    natural numbers and the square of the sum.
    """

    seq = xrange(1, seqmax + 1)
    return sum(seq) ** 2 - sum(x ** 2 for x in seq)


if __name__ == '__main__':
    assert answer(10) == 2640, 'failed small test with {}'.format(answer(10))
    print answer(100)
