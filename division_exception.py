def divide_numbers(number1,number2):
    try:
        print(number1/number2)
    except Exception:
        print("Cannot divide with zero or negative numbers")

#Tests
divide_numbers(55,11) # Output: 5.0 
divide_numbers(55,0)  # Output: Cannot divide with zero or negative numbers


