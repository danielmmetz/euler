# encoding=utf8
"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from itertools import permutations
from math import log

str_digit_set = set(str(num) for num in xrange(1, 10))

def gen_concat(num):
    str_num = str(num)
    for multiplier in xrange(2, 10):
        str_num += str(num*multiplier)
        if len(str_num) >= len(str_digit_set):
            break
    return int(str_num)


def is_pandigital(num):
    str_num = str(num)
    for int_len in xrange(1, len(str_num)/2+1):
        base = int(str_num[:int_len])
        if gen_concat(base) == num:
            return True
    return False


def answer():
    biggest = None
    for perm in permutations(xrange(1, 10)):
        num = reduce(lambda x, y: x*10+y, perm)
        if is_pandigital(num):
            biggest = max(biggest, num)
    return biggest


if __name__ == '__main__':
    print answer()