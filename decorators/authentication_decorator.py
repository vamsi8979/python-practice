authenticated = False

def authentication_decorator(func):
    def wrapper(*args, **kwargs):
        if authenticated:
            return func(*args, **kwargs)
        else:
            raise Exception("Access denied. Please authenticate.")
    return wrapper

# Example function
@authentication_decorator
def sensitive_operation():
    return "Sensitive information"

# Test cases
authenticated = True
result = sensitive_operation()
print(result)  # Output: Sensitive information

authenticated = False
try:
    result = sensitive_operation()
    print(result)  # This line won't be reached
except Exception as e:
    print(str(e))  # Output: Access denied. Please authenticate.
