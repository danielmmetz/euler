#!/usr/local/bin/python3
"""
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""
import functools


@functools.lru_cache(None)
def fib(n):
    """ generates the nth Fibonacci number """
    return fib(n - 2) + fib(n - 1) if n >= 2 else 1


def answer(limit):
    """ sums the even-valued Fibonacci terms not exceeding limit """
    fibs = []
    for potential_fib in (fib(n) for n in range(limit)):
        if potential_fib < limit:
            fibs.append(potential_fib)
        else:
            break
    return sum(fib for fib in fibs if not fib % 2)


if __name__ == '__main__':
    print(answer(4000000))
