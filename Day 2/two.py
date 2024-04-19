def concatenate_strings(*s):
    result = set()
    for i in s:
        result |= i
    return result

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
result = concatenate_strings(set1, set2, set3)
print(result)

s = 'Hello'
print(len(s))
def occurence_of_character(s):
    all_freq = {}
    for i in s:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq

print(occurence_of_character(s))

def palindrome(s):
    return s == s[::-1]

def most_frequent(s):
    d = occurence_of_character(s)
    d = list(d.items())
    d.sort(key=lambda x: x[1])
    return d[-1]

print(palindrome(s))
print(most_frequent(s))

# Write a program to make a new string with all the consonents deleted from the string
c =  "Hello, have a good day"
def delete_consonent(s):
    vowel = 'aeiouAEIOU'
    return ''.join(char for char in s if char in vowel)

print(delete_consonent(c))