"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

from prime import prime


def answer(num):
    """ returns the num-th prime """
    return prime(num - 1)


if __name__ == '__main__':
    assert answer(6) == 13, 'failed small test'
    print answer(10001)
