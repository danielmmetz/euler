# encoding=utf8
"""
In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1*£1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p

How many different ways can £2 be made using any number of coins?
"""

def answer(target, coins):
    num_ways = [1] + [0] * target
    for coin in coins:
        for mini_target in xrange(target+1):
            if coin <= mini_target:
                num_ways[mini_target] += num_ways[mini_target-coin]
    return num_ways[-1]


if __name__ == '__main__':
    print answer(200, [1, 2, 5, 10, 20, 50, 100, 200])

