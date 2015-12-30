"""
2^{15} = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^{1000}?
"""

def power_two(exp):
    return 1 << exp

def digit_sum(num):
    return sum(int(digit) for digit in str(num))

if __name__ == '__main__':
    print digit_sum(power_two(1000))