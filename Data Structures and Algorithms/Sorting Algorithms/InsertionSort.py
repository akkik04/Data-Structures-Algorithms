# AKSHITH K
# INSERTION SORT IMPLEMENTED IN PYTHON.

def insertion_sort(list):

    # variable to store the length of the list.
    x = len(list)

    # iterating through the list for the number of elements from index 1.
    for i in range(1, x):

        # while loop to determine if number on the left is larger than number on the right, while restricting negative indexing (i > 0).
        while list[i-1] > list[i] and i > 0:

            # swapping method.
            list[i], list[i-1] = list[i-1], list[i]

            # continuing algorithm.
            i = i -1
    return(list)

# DRIVER CODE FOR TESTING THE ALGORITHM.
list = [9, 1, 4, 3, 6, 8, 5, 0, 2, 7]
print("The sorted list is: ", insertion_sort(list))
