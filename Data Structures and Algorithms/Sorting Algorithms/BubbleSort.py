# AKSHITH K
# BUBBLE SORT IMPLEMENTED IN PYTHON.

def bubblesort(list):

    # variable to store length of the list.
    x = len(list)

    # iterating through the list for the amount of elements.
    for i in range (0, x):

        # determining the adjacent elements.
        for j in range (0, x - 1):

            # swapping method.
            if list[j] > list[j+1]:

                list[j], list[j+1] = list[j+1], list[j]
    return(list)
                    
# DRIVER CODE FOR TESTING THE ALGORITHM.
list = [0, 2, 6, 1, 9, 8, 7, 3, 5, 4]
print("The list sorted is: ", bubblesort(list))
