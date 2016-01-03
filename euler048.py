"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 10001000.
"""


def answer(bound):
    total = 0
    for num in xrange(1, bound+1):
        total += num**num
        total %= 10**10
    return total


if __name__ == '__main__':
    print answer(1000)
