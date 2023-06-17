def divide_numbers(number1, number2):
    try:
        result = number1 / number2
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except Exception as e:
        print("An error occurred:", str(e))
    else:
        print("No Exceptions were raised")
    finally:
        print("End of Method")
# Test Cases
test_cases = [
    (10,2),
    (7,0),
    (12,'4')
]

for i, (number1, number2) in enumerate(test_cases):
    print(f"Test Case {i + 1}")
    print("Input:", number1,number2)
    print("Output:", divide_numbers(number1, number2))
    print()

