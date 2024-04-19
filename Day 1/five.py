def factorial(d):
    if d == 1:
        return 1
    return d * factorial(d-1)

print(factorial(6))