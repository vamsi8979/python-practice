def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Test Cases
test_cases = [
    "home one",
    "maxima",
    "cook",
    "lumos",
    "patronum"
]

for i, string in enumerate(test_cases):
    print("Test Case", i+1)
    print("Input:")
    print("String:", string)
    char_count = count_characters(string)
    print("Character Count:", char_count)
    print()

