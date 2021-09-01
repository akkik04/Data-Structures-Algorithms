# AKSHITH K
# BUBBLE SORT IMPLEMENTED IN PYTHON.

def bubblesort(list, n):

    # iterating through the list for the amount of elements.
    for i in range (0, n):

        # creating a variable to track if we have swapped. Swapped is set to 'False'.
        swapped = False

        # determining the adjacent elements.
        for j in range (0, n - i - 1):

            # swapping method.
            if list[j] > list[j+1]:

                list[j], list[j+1] = list[j+1], list[j]

                # setting the boolean swapped to 'True' because we have swapped.
                swapped = True

        # checking if we have not swapped (making sure that swapped != True), so that we can simply break out and
        if not swapped:

            # breaking out.
            break   
    
    # returning the sorted list.
    return(list)
                    
# DRIVER CODE FOR TESTING THE ALGORITHM.
list = [0, 2, 6, 1, 9, 8, 7, 3, 5, 4]
n = len(list)
print("The list sorted is: ", bubblesort(list, n))
