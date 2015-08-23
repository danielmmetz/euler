"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from prime import prime


def answer(num):
    """ returns the sum of all primes below num """
    def primes_upto(num):
        """ returns a generator that iterates over all primes up to num """
        counter = 0
        while True:
            if prime(counter) >= num:
                break
            yield prime(counter)
            counter += 1

    return sum(primes_upto(num))


if __name__ == '__main__':
    assert answer(10) == 17, 'failed small test with {}'.format(answer(10))
    print answer(2000000)
