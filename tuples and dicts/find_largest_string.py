def find_largest_string(dictionary):
    max_length = 0
    largest_string = ""

    for key in dictionary.keys():
        if len(key) > max_length:
            max_length = len(key)
            largest_string = key
        elif len(key) == max_length:
            largest_string += ", " + key

    return largest_string


# Test Cases
test_cases = [
    {"write": "book", "watch": "movie", "play": "games", "listen": "songs"},
    {"coding": 1, "maxima": 2, "encode": 3, "private": 4, "limited": 5},
    {"kick": "raviteja", "simha": "balakrishna", "singam": "surya", "brothers": "surya"},
    {"apple": "red", "guava": "green", "grapes": "black", "watermelon": "green"},
    {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5},
]

for i, dic in enumerate(test_cases):
    print("Test Case", i+1)
    print("Input:")
    print(dic)
    largest_string = find_largest_string(dic)
    print("Largest String:", largest_string)
    print()

