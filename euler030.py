"""
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + ^4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""


def check(number, power):
    attempt = sum(int(num) ** power for num in str(number))
    return number == attempt


def calc_max_digits(power):
    BIGGEST_DIGIT = 9
    max_digits = 1
    while max_digits*BIGGEST_DIGIT**power > 10**max_digits:
        max_digits += 1
    return max_digits


def answer(power):
    max_digits = calc_max_digits(power)
    return sum(num for num in xrange(2, 10**max_digits) if check(num, power))


if __name__ == '__main__':
    print answer(5)