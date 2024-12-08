from functools import reduce
def filter_func(predicate, sequence):
    def reducer(acc, item):
        if predicate(item):
            acc.append(item)
        return acc
    return reduce(reducer, sequence, [])
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = filter_func(lambda x: x % 3 == 0, numbers)
print(result)