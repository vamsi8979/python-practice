def sort_array(array):
    temp = 0
    for i in range( 0, len(array) ):
        for j in range (i+1, len(array) ):
            if( array[i] > array[j] ):
                array[i],array[j] = array[j],array[i] #swapping
                swapped = True
        # If no swaps occurred in the last iteration, the array is already sorted
        if not swapped:
            break
    return array

# Tests
array = [9, 5, 2, 8, 1, 7]
print(sort_array(array))
# Expected output: [1, 2, 5, 7, 8, 9]

array = [64, 34, 25, 12, 22, 11, 90]
print(sort_array(array))
# Expected output: [11, 12, 22, 25, 34, 64, 90]

array = [12,73,91,82,816,826,6,65]
print(sort_array(array))
# Expected output: [6, 12, 65, 73, 82, 91, 816, 826]

