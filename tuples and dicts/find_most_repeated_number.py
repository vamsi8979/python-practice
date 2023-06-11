def find_most_repeated_number(lst):
    num_count = {}

    # Count the occurrences of each number in the list
    for num in lst:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    # Find the most repeated numbers
    max_count = max(num_count.values())
    most_repeated_numbers = [num for num, count in num_count.items() if count == max_count]

    return most_repeated_numbers


# Test Cases
test_cases = [
    [1, 2, 3, 4, 2, 3, 3],
    [23, 46, 16, 5, 16, 23, 5, 16, 5],
    [1, 2, 2, 1, 5, 2, 6],
    [1, 2, 3, 4, 3, 2, 2],
]

for i, lst in enumerate(test_cases):
    print("Test Case", i+1)
    print("Input:")
    print(lst)
    most_repeated_numbers = find_most_repeated_number(lst)
    print("Output:")
    print("Most repeated number(s):", ", ".join(str(num) for num in most_repeated_numbers))
    print()

