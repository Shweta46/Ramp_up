l = (1, 2, 3, 4, 5, 1, 1, 2, 3)
def repeated_elements(d):
    all_ = {}
    for i in l:
        if i in all_:
            all_[i] += 1
        else:
            all_[i] = 1
    for i in all_:
        if all_[i] > 1:
            print(i)

print(repeated_elements(l))

l = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

def tuple_to_dictionary(d):
    return {key: value for key, value in l}

print(tuple_to_dictionary(l))

l1 = (1, 2, 3)
l2 = (4, 5, 6)
def concatenate(t1, t2):
    l1 = list(t1)
    l2 = list(t2)
    l1.extend(l2)
    return tuple(l1)

def concatenate2(t1, t2):
    return t1 + t2

print(concatenate(l1, l2))