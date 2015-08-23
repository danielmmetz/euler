"""
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


def gcd(a, b):
    """ returns the greatest common divisor of a and b """
    return b and gcd(b, a % b) or a


def lcm(a, b):
    """ returns the least common denominator of a and b """
    return a * b / gcd(a, b)


def answer(seqmax):
    """
    returns the smallest positive number evenly divisible by all elements in
    {1, 2, ..., seqmax}
    """
    ans = 1
    for elem in xrange(1, seqmax + 1):
        ans = lcm(ans, elem)

    return ans


if __name__ == '__main__':
    assert answer(10) == 2520, 'failed small test with {}'.format(answer(10))
    print answer(20)
