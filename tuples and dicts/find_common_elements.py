def find_common_elements(list1, list2, list3):
    common_elements = []
    for element in list1:
        if element in list2 and element in list3:
            common_elements.append(element)
    return common_elements

# Test Cases
test_cases = [
    ([16, 23, 8, 9, 6, 18, 10], [18, 9, 43, 24, 12, 34], [13, 84, 9, 34, 18]),
    ([1, 2, 3, 4, 5, 6], [9, 8, 6, 2, 4, 7], [1, 2, 4, 6, 7]),
    ([23, 18, 46, 9, 5], [5, 82, 91, 39], [35, 46, 5]),
    ([1, 2, 3], [2, 3, 4], [3, 4, 5]),
    ([10, 20, 30], [30, 40, 50], [50, 60, 70]),
]

for i, (list1, list2, list3) in enumerate(test_cases):
    print("Test Case", i+1)
    print("Input:")
    print("List 1:", list1)
    print("List 2:", list2)
    print("List 3:", list3)
    common_elements = find_common_elements(list1, list2, list3)
    print("Common Elements:",common_elements)
    print()

