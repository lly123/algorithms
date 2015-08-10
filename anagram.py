__author__ = 'richard'

from collections import defaultdict


def anagram(w1, w2):
    def word2dict(w):
        def inc(d, a):
            d[a] += 1
            return d
        return reduce(inc, w, defaultdict(int))
    return word2dict(w1) == word2dict(w2)

print(anagram('listen', 'silent'))