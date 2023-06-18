import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time} seconds")
        return result
    return wrapper

# Example function
@timer_decorator
def multiply_numbers(a, b):
    time.sleep(2)  # Simulate a time-consuming operation
    return a * b

@timer_decorator
def power_of_number(base, exponent):
    time.sleep(3)  # Simulate a time-consuming operation
    return base ** exponent

# Test cases
result = multiply_numbers(5, 10)
print(result)  # Output: 50

result = power_of_number(2, 8)
print(result)  # Output: 256
