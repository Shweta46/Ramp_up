import math
print(dir(math))

def my_function():
    print("hello world!")

# This allows you to include code that should only run when the script is executed directly,
# not when it's imported as a module.
if __name__ == '__main__':
    my_function()

