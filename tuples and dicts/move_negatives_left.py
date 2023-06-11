def move_negatives_left(array):
    j=0
    for i in range(0,len(array)):
        if(array[i]<0):
            array[i],array[j]=array[j],array[i]
            j+=1
    return array

def run_tests(test_cases_array):
    for test_case in test_cases_array:
        print("Input:", test_case)
        result = move_negatives_left(test_case)
        print("Output:", result)
        print()
    

# Test cases
test_cases = [
    [-10, 4, 18, -19, 73, -21, 12, -2, 34, -43],
    [34, 56, 6, -3, 8, -32, -4, 94],
    [-1, -2, -3, -4, -5],
    [141, 32, -31, 4, -51],
    [1, 2, 3, 4, 5],
]

run_tests(test_cases)


