__author__ = 'lly'

from numpy import *
import sys

a = [1, 4, 8, 1, 9, 6, 2, 3]


def split(n, l):
    return 0 if l == 0 else sys.maxint if len(n) < 3 else \
        min([v + t for (i, v) in enumerate(n[1:-1]) for t in [split(n[i + 2:], l - 1)]])

print(split(a, 2))




