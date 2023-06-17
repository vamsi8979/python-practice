def divide_numbers(number1, number2):
    try:
        result = number1 / number2
        return result
    except (ZeroDivisionError,ValueError) as e:
        print("Type type(e) :",type(e))
        print("Type e.__class__ :",e.__class__)
        print("Name e.__class__.__name__ :",e.__class__.__name__)
        print("Description :",e)

# Test cases
print("7/0 : ",divide_numbers(7, 0))

