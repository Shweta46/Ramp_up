def contains_this(l, element):
    # for i in l:
    #     if i == element:
    #         return 1
    if element in l:
        return 1
    return 0
l = [1,1, 2,2, 4, 3, 5, 100, 80,9, 10, 66]
print(contains_this(l, 10))

