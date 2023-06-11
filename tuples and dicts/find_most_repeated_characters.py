def find_most_repeated_characters(string):
    char_count = {}
    max_count = 0
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        if char_count[char] > max_count:
            max_count = char_count[char]

    most_repeated_chars = [char for char, count in char_count.items() if count == max_count]
    return most_repeated_chars

# Test Cases
test_cases = [
    "success",
    "rubber",
    "homeone",
    "lumos",
    "patronaam"
]

for i, string in enumerate(test_cases):
    print("Test Case", i+1)
    print("Input:")
    print("String:", string)
    char = find_most_repeated_characters(string)
    print("Most Repeated Character:", char)
    print()

