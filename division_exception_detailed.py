def divide_numbers(number1, number2):
    try:
        result = number1 / number2
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except Exception as e:
        print("An error occurred:", str(e))

# Test cases
print("Out put: ",divide_numbers(10, 2))  # Output: 5.0
print("Out put: ",divide_numbers(7, 0))   # Output: Error: Division by zero is not allowed!
print("Out put: ",divide_numbers(12, '4'))  # Output: An error occurred: unsupported operand type(s) for /: 'int' and 'str'


