"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def answer(num):
    """
    returns the sum of all multiples of 3 or 5 below num
    """
    return sum(n for n in xrange(num) if not n % 3 or not n % 5)


if __name__ == '__main__':
    assert answer(10) == 23
    print answer(1000)
