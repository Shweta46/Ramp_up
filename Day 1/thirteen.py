l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def max_sum_sublist(d):
    current = 0
    maximum = 0
    for i in range(len(l)):
        current += d[i]
        if current < 0:
            current = 0
        if current > maximum:
            maximum = current
    return maximum

print(max_sum_sublist(l))
