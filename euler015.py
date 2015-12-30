#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Starting in the top left corner of a 2 x 2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?
"""

from functools import lru_cache
import sys
from scipy.special import binom

@lru_cache(maxsize=None)
def num_paths(x, y):
  if x == 0 or y == 0:
    return 1

  return num_paths(x-1, y) + num_paths(x, y-1)

def faster(x, y):
    return int(binom(x+y, x))

if __name__ == '__main__':
  try:
    x, y = int(sys.argv[1]), int(sys.argv[2])
    print(faster(x, y))
  except:
    pass