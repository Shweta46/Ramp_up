file = open('this.txt', 'r+')
# for each in file:
#     print(each)

print(file.read())

with open('this.txt') as file:
    data = file.read()
print(data)

file = open('this.txt', 'r')
print(file.read(10)) # reads the first n characters

with open('this.txt', 'r') as file:
    data = file.readlines() # reads all lines from the file and stores them in a list 'data'
    print(data)
    for line in data:
        word = line.split()
        print(word)

with open('this.txt', 'w') as file:
    file.write('Hello world')
    file.flush()

file = open('this.txt', 'r')
print(file.writable())  # Outputs False, because the file is opened in read mode ('r')
file.close()

file = open('this.txt', 'w')
print(file.writable())  # Outputs True, because the file is opened in write mode ('w')
file.close()

with open('this.txt', 'r+') as file:
    lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
    file.writelines(lines)
    file.read()