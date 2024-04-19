def sum_of_digits_in_a_number(d):
    c = [int(i) for i in str(d)]
    p = 0
    for i in c:
        p += i
    return p

print(sum_of_digits_in_a_number(122))