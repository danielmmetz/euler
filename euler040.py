"""
An irrational decimal fraction is created by concatenating the positive
integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the
following expression.

    d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000
"""


from itertools import count


def answer(dns):
    product, ndigits, target = 1, 0, dns.pop(0)
    for num in count(1):
        if target <= ndigits:
            target = dns.pop(0)
        str_num = str(num)
        if target <= ndigits + len(str_num):
            product *= int(str_num[target-ndigits-1])
            if not dns:
                return product
        ndigits += len(str_num)


if __name__ == '__main__':
    print answer([10**exp for exp in xrange(7)])
