def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test cases
test_cases = [
    [-2, 1, -3, 4, -1, 3, 1, -5],
    [-2, 4, 9, -1, 3, -5, 8, -3, -1],
    [-2, 4, 9, -1, 3, -5, 8, -3, -1, 8],
    [23, -2, 4, 1, -1],
    [10, -5, 7, -2, 3, 1, -1, 4, -3, 2],
    [1, 2, 3, 4, 5],
]

for i, arr in enumerate(test_cases):
    print(f"Test Case {i + 1}")
    print("Array:", arr)
    max_sum = max_subarray_sum(arr)
    print("Maximum Subarray Sum Is:", max_sum)
    print()

