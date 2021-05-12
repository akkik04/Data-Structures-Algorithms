# AKSHITH K
# BINARY SEARCH IMPLEMENTED IN PYTHON.

def binary_search(arr, target):

    # declaring the default minimum and maximum values of the array.
    min_index = 0
    max_index = len(arr) - 1

    # while-loop to iterate for the time that the minimum_value is lower than the maximum_value.
    while min_index <= max_index:

        # finding midpoint in array.
        midpoint = (min_index + max_index) // 2
        midpoint_value = arr[midpoint]

        # if-statement to return the index if target is found, or apply the appropriate changes till the target is found.
        if midpoint_value == target:

            return midpoint

        elif target < midpoint_value:

            max_index = midpoint - 1
        
        else:
            min_index = midpoint + 1

    # returning 'None' if the element is not present in the array.
    return None

# DRIVER CODE FOR TESTING THE ALGORITHM.
arr = [2, 6, 9, 17, 22, 32, 38, 40, 43, 56]
target = 43
print("The desired element is present at index: " + str(binary_search(arr, target)))