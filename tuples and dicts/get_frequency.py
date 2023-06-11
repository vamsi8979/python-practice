def get_frequency(tuple):
    frequency = {}
    for value in tuple:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1
    return frequency

# Test cases
test_cases = [
    (1, 2, 3, 4, 5, 4, 3, 4, 2, 3),
    (23, 46, 23, 46, 23),
    (1, 2, 3, 2, 2),
    (10, 20, 30, 40, 30, 20, 10),
    (5, 5, 5, 5, 5),
]

for i, tuple in enumerate(test_cases):
    print(f"Test Case {i + 1}")
    print("Tuple:", tuple)
    print("Frequency:", get_frequency(tuple))
    print()

