def largest_smallest(l):
    return max(l), min(l)

print(largest_smallest(l))

def remove_duplicates(l):
    l = set(l)
    return list(l)
l = [1,1, 2,2, 4, 3, 5, 100, 80,9, 10, 66]
print(remove_duplicates(l))