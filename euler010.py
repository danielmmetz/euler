"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from prime import prime, _refresh, prime_list


def answer(num):
    """ returns the sum of all primes below num """
    _refresh(num)
    return sum(prime_list)


if __name__ == '__main__':
    print(answer(2000000))
