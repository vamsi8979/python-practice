import math
import datetime
import random

def math_module():
    print("Using math module")
    print("   Square of 16 :",math.sqrt(16))
    print("   Log of 10 :",math.log(10))

def datetime_module():
    print("Using datetime module")
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    print("   DateTime : ",current_datetime)

    date = datetime.datetime(2022, 5, 15)
    formatted_date = date.strftime("%d-%b-%Y")
    print("   Formatted Date: ",formatted_date)

def random_module():
    print("Using random module")
    # Generate a random integer between 1 and 10
    random_number = random.randint(1, 10)
    print("   First random number : ",random_number)
    random_number = random.randint(1, 10)
    print("   Second random number : ",random_number)

    # Shuffle a list randomly
    my_list = [1, 2, 3, 4, 5]
    random.shuffle(my_list)
    print("   Shuffled list : ",my_list)  # Output: [3, 2, 5, 1, 4]
math_module()
datetime_module()
random_module()

