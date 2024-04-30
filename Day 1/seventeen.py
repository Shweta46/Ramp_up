l = [1,1, 2,2, 4, 3, 5, 100, 80,9, 10, 66]
def empty_or_not(l):
    if len(l) == 0:
        return 1
    else:
        return 0
print(empty_or_not(l))
def sum_list(l):
    p = 0
    summation = sum(l)
    print(summation)
    for i in l:
        p += i
    return p
sum_list(l)