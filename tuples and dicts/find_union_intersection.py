def find_union_intersection(list1, list2):
    # Combine the lists and remove duplicates
    union = list(set(list1 + list2))

    # Find the intersection between the lists
    intersection = list(set(list1) & set(list2))

    return union, intersection


# Test Cases
test_cases = [
    ([1, 2, 2, 3, 4], [2, 5, 8, 9, 23]),
    ([23, 45, 56, 67, 78], [1, 2, 23, 45, 55, 66, 77]),
    ([1, 2, 2, 3, 4, 5, 6], [2, 4, 6, 8, 9]),
    ([1, 14, 23, 35, 46, 46], [2, 14, 25, 35, 46]),
]

for i, (list1, list2) in enumerate(test_cases):
    print("Test Case", i+1)
    print("Input:")
    print("List 1:", list1)
    print("List 2:", list2)
    union, intersection = find_union_intersection(list1, list2)
    print("Output:")
    print("Union of list:", ", ".join(str(num) for num in union))
    print("Intersection of list:", ", ".join(str(num) for num in intersection))
    print()

