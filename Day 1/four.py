
def sum_of_digits_in_a_number(d):
    n = str(d)
    l = [int(i) for i in n]
    return sum(l)

print(sum_of_digits_in_a_number(12))