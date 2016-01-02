"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note
the following:

d_2 d_3 d_4  = 406 is divisible by 2
d_3 d_4 d_5  = 063 is divisible by 3
d_4 d_5 d_6  = 635 is divisible by 5
d_5 d_6 d_7  = 357 is divisible by 7
d_6 d_7 d_8  = 572 is divisible by 11
d_7 d_8 d_9  = 728 is divisible by 13
d_8 d_9 d_10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""


from itertools import permutations


def digits_to_num(digits):
    return reduce(lambda x, y: x*10+y, digits)


def has_property(digits):
    valid = True
    valid = valid and not digits_to_num(digits[1:4])%2
    valid = valid and not digits_to_num(digits[2:5])%3
    valid = valid and not digits_to_num(digits[3:6])%5
    valid = valid and not digits_to_num(digits[4:7])%7
    valid = valid and not digits_to_num(digits[5:8])%11
    valid = valid and not digits_to_num(digits[6:9])%13
    valid = valid and not digits_to_num(digits[7:10])%17
    return valid


def answer():
    return sum(digits_to_num(perm) for perm in permutations(xrange(10))
                                   if has_property (perm))


if __name__ == '__main__':
    print answer()
