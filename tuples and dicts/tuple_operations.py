def get_positive_values(tuples):
    positive_tuples = [tpl for tpl in tuples if all(num > 0 for num in tpl)]
    return tuple(positive_tuples)

def get_negative_values(tuples):
    negative_tuples = [tpl for tpl in tuples if all(num < 0 for num in tpl)]
    return tuple(negative_tuples)

def get_even_numbers(tuples):
    even_tuples = [tpl for tpl in tuples if all(num % 2 == 0 for num in tpl)]
    return tuple(even_tuples)

def get_odd_numbers(tuples):
    odd_tuples = [tpl for tpl in tuples if all(num % 2 != 0 for num in tpl)]
    return tuple(odd_tuples)

def get_divisible_by_key(tuples, key):
    divisible_tuples = [tpl for tpl in tuples if all(num % key == 0 for num in tpl)]
    return tuple(divisible_tuples)

# Test cases
test_cases = [
    ([(8, 24, 32), (-1, -3, 5)], 8),
    ([(1, 5, 7), (-5, -10, -15), (2, 4, 5)], 6),
    ([(3, 9, 15), (2, 4, 8), (-1, -3, -5)], 3),
    ([(-2, -4, 6), (5, 10, 15), (-12, -18, -10), (23, 34, 35), (75, 45, 55)], 5),
    ([(2, 4, 6), (8, 10, 12), (14, 16, 18)], 2),
]

for i, (tuples, key) in enumerate(test_cases):
    print(f"Test Case {i + 1}")
    print("Tuple:", tuples)
    print("Key:", key)
    print("The all positive values in tuple:", get_positive_values(tuples))
    print("The all negative values in tuple:", get_negative_values(tuples))
    print("The all even numbers in tuple:", get_even_numbers(tuples))
    print("The all odd numbers in tuple:", get_odd_numbers(tuples))
    print("The elements in the tuple divisible by given key element:", get_divisible_by_key(tuples, key))
    print()

