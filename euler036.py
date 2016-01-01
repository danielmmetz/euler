"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""


def is_double_palindrome(num):
    b2num = bin(num)
    return str(num) == str(num)[::-1] and b2num[2:] == b2num[:1:-1]


def answer(bound):
    return sum(num for num in xrange(bound) if is_double_palindrome(num))


if __name__ == '__main__':
    print answer(1000000)
