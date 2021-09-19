# AKSHITH K
# BUBBLE SORT IMPLEMENTED IN PYTHON RECURSIVELY.

def bubblesort(arr, n):

    # checking if the array does not need to be sorted and has a length of 1.
    if n <= 1:

        return

    # creating a for-loop to iterate for the elements in the array.
    for i in range(0, n - 1):

        # creating an if-statement to check for the element not being in the right position.
        if arr[i] > arr[i + 1]:

            # code to perform the swapping method.
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # recursively calling the function for the sorting.
    return bubblesort(arr, n - 1)

# DRIVER CODE FOR TESTING THE ALGORITHM.
arr = [4, 9, 1, 3, 0, 2, 6, 8, 5, 7]
n = len(arr)
bubblesort(arr, n)
print(arr)
