__author__ = 'richard'

from collections import Counter
import numpy as np

# Age, Income, Car, Work hours, Home distance, Education Degree, Height
training_set = [
    ('Possible1', [36, 400000, 160000, 8, 178]),
    ('Impossible1', [20, 200000, 0, 8, 180]),
    ('Possible2', [25, 800000, 400000, 6, 180]),
    ('Impossible2', [40, 600000, 600000, 8, 175]),
    ('Possible3', [28, 1000000, 0, 12, 178]),
    ('Impossible3', [30, 100000, 1000000, 1, 178]),
    ('Impossible4', [50, 10000000, 1000000, 2, 175]),
    ('Impossible5', [18, 10000000, 3000000, 12, 180]),
    ('Impossible6', [28, 1000000, 2000000, 20, 170]),
    ('Possible4', [26, 500000, 200000, 8, 172])
]


def normalize(p, arr):
    arr = np.vstack((arr, p))
    max = arr.max(axis=0)
    min = arr.min(axis=0)
    return (arr - min * 1.0) / (max - min)


def sort(arr, labels):
    def distance(p1, p2):
        return np.sum((p1 - p2) ** 2) ** 0.5

    p = arr[-1]
    arr = zip(arr[:-1], labels)
    sorted_arr = sorted(arr, key=lambda x: distance(x[0], p))
    return map(lambda x: x[1], sorted_arr)


def knn(p, s, k):
    def majority_vote(sorted_labels):
        counter = Counter(sort(normalize(p, np.array(values)), sorted_labels))
        winner, winner_count = counter.most_common(1)[0]
        num_winners = [v for v in counter.values() if v == winner_count]
        return winner if len(num_winners) == 1 else majority_vote(sorted_labels[:-1])

    labels = map(lambda x: x[0], s)
    values = map(lambda x: x[1], s)
    return majority_vote(sort(normalize(p, np.array(values)), labels)[:k])

print(knn([10, 500000, 200000, 10, 176], training_set, 3))
# labels = sort(normalize([7, 8, 9], np.array([[6, 7, 8], [1, 2, 3], [4, 5, 6]])), ['a', 'b', 'c'])
# print(Counter(labels))



