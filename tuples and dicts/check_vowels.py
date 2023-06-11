def check_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for char in string:
        if char.lower() in vowels:
            print(char, "is a vowel")
        else:
            print(char, "is not a vowel")

# Test Cases
test_cases = [
    "coding maxima",
    "python",
    "container",
    "sheep",
    "programming",
]

for test_case in test_cases:
    print("Input:", test_case)
    check_vowels(test_case)
    print()

