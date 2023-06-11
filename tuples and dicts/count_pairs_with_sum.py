def count_pairs_with_sum(array, target_sum):
    count = 0
    seen = set()

    for num in array:
        complement = target_sum - num
        if complement in seen:
            count += 1
        seen.add(num)

    return count

# Test cases
test_cases = [
    ([1, 17, 5, -23, 73, -1, 51, 23, 45], 50),
    ([3, 5, 8, 82, 7, -1, -6, 12], 6),
    ([21, 2, 75, -52, 23, 23, 11, 12, 9, 14, -5, 28, -6], 23),
    ([10, 20, 30], 40),
    ([-5, -5, -5, -5, -5], -10),
]

for i, (array, target_sum) in enumerate(test_cases):
    print(f"Test Case {i + 1}")
    print("List:", array)
    print("Target Sum:", target_sum)
    pair_count = count_pairs_with_sum(array, target_sum)
    print("Number of pairs count:", pair_count)
    print()

