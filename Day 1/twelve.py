b = {'a': 10, 'b': 5, 'c': 20, 'd': 10, 'e': 100, 'f': 12}

def maximum1(d):
    max_ = -9999999
    a = list(d.items())
    l = len(a)
    for i in range(l):
        if a[i][1] > max_:
            max_ = a[i][1]
    for i, j in d.items():
        if j == max_:
            return i

def maximum_(d):
    d = list(b.items())
    p = max(d, key= lambda x:x[1])
    print('The list:', p)
print(maximum_(b))

my_tuple = ('apple', 'banana')
fruit1, fruit2 = my_tuple
print(fruit1)  # Output: 'apple'
print(fruit2)  # Output: 'banana'

def maximum(d):
    max_val = float('-inf')
    max_key = None
    for key, value in d.items():
        if value > max_val:
            max_val = value
            max_key = key
    return max_key

print(maximum(b))

c = [1, 12, 4, 5]
c.sort()
print('sorted c', c)
print(type(c))

intervals = [(1, 3), (2, 6), (15, 18), (8, 10)]
def merged(d):
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    merged_intervals = [intervals[0]]
    print(merged_intervals)
    for interval in intervals[1:]:
        if interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1]=merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1])
        else:
            merged_intervals.append(interval)
    return merged_intervals

print(merged(intervals))
output = [(1, 6), (8, 10), (15, 18)]


