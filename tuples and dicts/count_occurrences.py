def count_occurrences(numbers):
    occurrence_count = {}
    for number in numbers:
        if number in occurrence_count:
            occurrence_count[number] += 1
        else:
            occurrence_count[number] = 1
    return occurrence_count

# Test Cases
test_cases = [
    [9, 18, 23, 16, 5, 18, 23, 5, 5],
    [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2],
    [23, 54, 87, 23, 54, 98, 23],
    [0, 0, 0, 0, 0, 0],
    [1, 2, 3, 4, 5],
]

for i, numbers in enumerate(test_cases):
    print("Test Case", i+1)
    print("Input:")
    print("Numbers:", numbers)
    occurrence_count = count_occurrences(numbers)
    print("Occurrence Count:", occurrence_count)
    print()

