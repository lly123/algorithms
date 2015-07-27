from functools import *


def flat_map(fn, l):
    return reduce(list.__add__, map(fn, l))


def safe(a, i, n):
    return True if len(a) == 0 else (a[-1] != i and a[-1] - n != i and a[-1] + n != i and safe(a[:-1], i, n + 1))


def eight_queens():
    return reduce(lambda s, _: flat_map(lambda x: [x + [y] for y in range(8) if safe(x, y, 1)], s),
                  [x for x in range(7)], [[x] for x in range(8)])


ret = eight_queens()
print(len(ret))
print(eight_queens())

