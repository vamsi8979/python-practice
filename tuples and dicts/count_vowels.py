def count_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

# Test cases
test_cases = [
    "coding maxima",
    "python",
    "aeiou",
    "Lorem ipsum dolor sit amet",
    "Quick brown fox jumps over the lazy dog",
    "1234567890",
]

for i, string in enumerate(test_cases):
    print(f"Test Case {i + 1}")
    print("String:", string)
    print("Number of vowels:", count_vowels(string))
    print()

