l = [1,1, 2,2, 4, 3, 5, 100, 80,9, 10, 66]
def sort_in_ascending(l):
    n = len(l)
    for i in range(n):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j+1], l[j] = l[j], l[j+1]
    return l

print(sort_in_ascending(l))