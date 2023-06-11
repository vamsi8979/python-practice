def find_unique_values_sum(lst):
    unique_values = {}

    # Count the occurrences of each value in the list
    for value in lst:
        if value in unique_values:
            unique_values[value] += 1
        else:
            unique_values[value] = 1

    # Sum the unique values that occur only once
    unique_values_sum = sum(key for key, count in unique_values.items() if count == 1)

    return unique_values_sum


# Test Cases
test_cases = [
    [1, 17, 5, -23, 23, -9, 5, 23, 20],
    [23, 18, 46, 16, 5, 46, 23, 18],
    [1, 2, 3, 4, 5, 4, 3, 8, 6],
    [12, 62, 82, 18, 12, 18],
]

for i, lst in enumerate(test_cases):
    print("Test Case", i+1)
    print("Input:")
    print(lst)
    unique_values_sum = find_unique_values_sum(lst)
    print("Output:")
    print("Unique values sum:", unique_values_sum)
    print()

