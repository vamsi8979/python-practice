import datetime

# Logging levels
LOG_LEVEL_INFO = 1
LOG_LEVEL_ERROR = 2

# Logging utility functions
def log_info(message):
    log_message(LOG_LEVEL_INFO, message)

def log_error(message):
    log_message(LOG_LEVEL_ERROR, message)

def log_message(log_level, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level = "INFO" if log_level == LOG_LEVEL_INFO else "ERROR"
    print(f"{timestamp} - {level} - {message}")

# Logging decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        log_info(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        log_info(f"Finished {func.__name__}")
        return result
    return wrapper

# Example functions
@log_decorator
def add_numbers(a, b):
    return a + b

@log_decorator
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        log_error("Error: Division by zero!")
        return None

# Test cases
result = add_numbers(2, 3)
print("Output :",result)

result = divide_numbers(10, 0)
print("Output :",result)
