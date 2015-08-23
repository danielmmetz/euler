"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def answer(num):
    """ finds the largest prime factor of num """
    test = 2

    while test * test < num:
        while not num % test:
            num /= test

        test += 1

    return num


if __name__ == '__main__':
    assert answer(13195) == 29, 'failed small test'
    print answer(600851475143)
