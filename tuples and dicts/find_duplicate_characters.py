def find_duplicate_characters(string):
    char_count = {}

    # Count the occurrences of each character in the string
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the duplicate characters with count > 1
    duplicate_chars = {char: count for char, count in char_count.items() if count > 1}

    return duplicate_chars


# Test Cases
test_cases = [
    "homeone",
    "Rubberball",
    "commit",
]

for i, string in enumerate(test_cases):
    print("Test Case", i+1)
    print("Input:")
    print(string)
    duplicate_chars = find_duplicate_characters(string)
    print("Output:")
    for char, count in duplicate_chars.items():
        print(char, "occurs", count, "times")
    print()

