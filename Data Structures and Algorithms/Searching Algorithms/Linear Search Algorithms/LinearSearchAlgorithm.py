# AKSHITH K
# LINEAR SEARCH IMPLEMENTED IN PYTHON.

def linear_search(arr, target):

    # creating a for-loop to iterate for the amount of elements present in the array.
    for i in range(len(arr)):

        # if-statement for checking if the target is found at any index, while returning the value of the index if it is found.
        if target == arr[i]:

            return i
        
    # returning 'None' if the element is not present in the array.
    return None

# DRIVER CODE FOR TESTING THE ALGORITHM.
arr = [1, 4, 6, 9, 16, 27, 32, 34, 66, 78]
target = 27
print("The element is present at index: " + str(linear_search(arr, target)))
