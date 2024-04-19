def os_error():
    try:
        with open('non_existent_file.txt', 'r') as file:
            content = file.read()
    except OSError as e:
        print(f'Error: {e}')

os_error()

def arithmetic_error():
    try:
        result = 10/0
    except ArithmeticError as e:
        print(f'Error: {e}')

arithmetic_error()

def zero_division_error():
    try:
        result = 10/0
    #     its a subdivision class of arithmetic error
    except ZeroDivisionError as e:
        print(f'Error: {e}')

zero_division_error()

def assertion_error():
    x = 10
    assert x < 0, 'x should be negative.'
# assertion_error()

def overflow_error():
    try:
        result = 2**100000
    except OverflowError as e:
        print(f'Error: {e}')

overflow_error()

