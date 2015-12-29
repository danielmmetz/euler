"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

   {20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

from collections import defaultdict
from math import sqrt

def answer(perimeter_limit):
    p_count = defaultdict(int)
    max_p, max_count = -1, -1

    max_side = int(perimeter_limit / (2 + sqrt(2)))
    for a in xrange(1, max_side):
        for b in xrange(a, perimeter_limit/2):
            c = int(sqrt(a**2 + b**2))
            p = a + b + c

            if a**2 + b**2 == c**2:
                p_count[p] += 1

            if p_count[p] > max_count:
                max_p, max_count = p, p_count[p]

    return max_p

if __name__ == '__main__':
    print answer(1000)