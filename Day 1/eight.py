'''
Write a Python program to count the frequency of elements in a list and store it as a dictionary, where the key is the element and the value is the frequency. For example, given the list [1, 2, 1, 3, 2, 1], the dictionary should be {1: 3, 2: 2, 3: 1}. How would you approach this problem?
'''
a = [1, 2, 1, 3, 2, 1]
def frequency(a):
    dict1 = {}
    for i in a:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1

print(frequency(a))
