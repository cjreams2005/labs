from functools import reduce

list_1 = ["a", "b", "c", "d", "e", "f"]
list_2 = [1, 2, 3, 4, 5]

def zipmap(key_list: list, value_list: list, override = False):
    if not override:
        if len(key_list)!= len(set(key_list)):
            return None
    zipped = zip(key_list, value_list)
    def reducer(acc, pair):
        key, value = pair
        if override or key not in acc:
            acc[key] = value
        return acc
    return reduce(reducer, zipped, {})

print(zipmap(list_1, list_2))