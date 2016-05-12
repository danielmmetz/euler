"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

from prime import isprime
from itertools import permutations, combinations_with_replacement
from functools import reduce


def digits_to_num(digits):
   return reduce(lambda x, y: x*10+y, digits)


def answer():
    for numbers in combinations_with_replacement(range(10), 4):
        perms_l = [digits_to_num(n) for n in permutations(numbers)]
        perms_s = set(perms_l)
        for fst_index, fst in enumerate(perms_l):
            if fst <= 1487: # rule out given value
                continue
            for snd_index in range(fst_index+1, len(perms_l)):
                snd = perms_l[snd_index]
                dif = snd-fst
                if dif == 0:
                    continue
                thrd = snd+dif
                if thrd in perms_s:
                    if all(isprime(n) for n in (fst, snd, thrd)):
                        return fst, snd, thrd


if __name__ == '__main__':
    print(answer())