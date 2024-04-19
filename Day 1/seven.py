def sum_of_series(n):
    result = 0
    for i in range(1, n+1):
        result += 1/i
    return result
print(sum_of_series(10))

def area_of_circle(r):
    return 3.14*(r**2)