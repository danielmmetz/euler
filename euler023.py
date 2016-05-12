"""
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

from prime import all_factors

def find_abundant_numbers(limit):
    abundant_numbers_lst = []
    abundant_numbers_set = set()
    for i in range(1, limit):
        factor_total = sum(all_factors(i)) - i
        if factor_total > i:
            abundant_numbers_lst.append(i)
            abundant_numbers_set.add(i)
    return abundant_numbers_lst, abundant_numbers_set

def answer(limit):
    abundant_numbers_lst, abundant_numbers_set = find_abundant_numbers(limit)
    valid = set(range(limit))
    for candidate in range(limit):
        for smaller in abundant_numbers_lst:
            if smaller > candidate:
                break
            if candidate - smaller in abundant_numbers_set:
                valid.remove(candidate)
                break
    return sum(valid)


if __name__ == '__main__':
    print(answer(28124))


