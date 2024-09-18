def make_set(data):
    set = []
    for value in data:
        if value not in set:
            set.append(value)
    return set

def is_set(data):
    set = []
    for value in data:
        if value not in set:
            set.append(value)
    if set == data:
        return True
    else:
        return False

def union(setA, setB):
    count = 0
    set_checkA = []
    set_checkB = []
    for value in setA:
        if value not in set_checkA:
            set_checkA.append(value)
    if set_checkA == setA:
        count += 0
    else:
        count += 1
    for value in setB:
        if value not in set_checkB:
            set_checkB.append(value)
    if set_checkB == setB:
        count += 0
    else:
        count += 1
    if count > 0:
        return []
    else:
        union_set = []
        for value in setA:
            if value not in union_set:
                union_set.append(value)
        for value in setB:
            if value not in union_set:
                union_set.append(value)
        return(union_set)

def intersection(setA, setB):
    count = 0
    set_checkA = []
    set_checkB = []
    for value in setA:
        if value not in set_checkA:
            set_checkA.append(value)
    if set_checkA == setA:
        count += 0
    else:
        count += 1
    for value in setB:
        if value not in set_checkB:
            set_checkB.append(value)
    if set_checkB == setB:
        count += 0
    else:
        count += 1
    if count > 0:
        return []
    else:
        intersection_set = []
        for value in setA:
            if value in setB:
                intersection_set.append(value)
        return(intersection_set)

print(union([4, 2, 3, 4, 7, 9], [2,3]))
