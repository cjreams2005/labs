
from functools import reduce
from collections import defaultdict

def group_by(func, sequence):
    grouped = defaultdict(list)
    def reducer(acc, item):
        key = func(item)
        acc[key].append(item)
        return acc
    result = reduce(reducer, sequence, grouped)
    return dict(result)
print(group_by(len, ["hi", "dog", "me", "bad", "good"]))