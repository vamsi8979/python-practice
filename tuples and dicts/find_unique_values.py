def find_unique_values(lst):
    value_count = {}

    # Count the occurrences of each value in the list
    for value in lst:
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1

    # Find the unique values that occur only once
    unique_values = [key for key, count in value_count.items() if count == 1]

    return unique_values


# Test Cases
test_cases = [
    [73, 63, 2, 2, 43, 23, 54, 43],
    [1, 2, 3, 4, 5, 4, 3, 7, 6],
    [23, 18, 46, 16, 5, 46, 23, 18],
    [12, 62, 82, 18, 12, 18],
]

for i, lst in enumerate(test_cases):
    print("Test Case", i+1)
    print("Input:")
    print(lst)
    unique_values = find_unique_values(lst)
    print("Output:")
    print("Unique values are:", ", ".join(str(value) for value in unique_values))
    print()

