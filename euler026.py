"""
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2     =   0.5
1/3     =   0.(3)
1/4     =   0.25
1/5     =   0.2
1/6     =   0.1(6)
1/7     =   0.(142857)
1/8     =   0.125
1/9     =   0.(1)
1/10    =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.
"""

from itertools import count


def cycle_length(n):
    if not n % 2:
        return cycle_length(n // 2)
    if not n % 5:
        return cycle_length(n // 5)
    for i in count(1):
        if not (pow(10, i) - 1) % n:
            return i


def answer(limit):
    num, length = 1, 1
    for n in range(1, limit):
        n_length = cycle_length(n)
        if n_length > length:
            num, length = n, n_length
    return num


if __name__ == '__main__':
    print(answer(1000))
