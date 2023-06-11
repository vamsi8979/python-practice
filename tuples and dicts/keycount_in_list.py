# Code
def KeyCount(array,n,key):
    count = 0
    for i in range(n):
        if key == array[i]:
            count += 1
    return count

# Tests
array = [12,64,64,17,82,82,91,72,17,82]
n = len(array)
key = 82

print(KeyCount(array,n,key))
# Expected output: 3

# we can also use python inbuilt method
print(array.count(key))
# Expected output: 3

array = [2, 4, 6, 2, 8, 2]
n = len(array)
key = 2
print(KeyCount(array, n, key))
# Expected output: 3

array = [1, 3, 5, 7, 9]
n = len(array)
key = 2
print(KeyCount(array, n, key))
# Expected output: 0

array = [10, 20, 30, 40, 50]
n = len(array)
key = 30
print(KeyCount(array, n, key))
# Expected output: 1

array = []
n = len(array)
key = 5
print(KeyCount(array, n, key))
# Expected output: 0

array = [1, 2, 3, 2, 4, 2, 5]
n = len(array)
key = 2
print(KeyCount(array, n, key))
# Expected output: 3
