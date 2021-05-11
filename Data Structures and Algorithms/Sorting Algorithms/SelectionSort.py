# AKSHITH K
# SELECTION SORT IMPLEMENTED IN PYTHON.

def selection_sort(list):

    # variable to store the length of the list.
    x = len(list)

    # creating a for-loop to iterate till the last index in the list.
    for i in range (0, x - 1):

        # creating a variable to store the current minimum value as the first index. 
        cur_min = i

        # nested for-loop to iterate for all the elements past the declared minimum value.
        for j in range(i + 1, x):
            
            # checking if any element past the declared minimum value is greater.
            if list[j] < list[cur_min]:
                
                # resetting the minimum value to 'j' if a lower value is found.
                cur_min = j

        # swapping method.       
        list[i], list[cur_min] = list[cur_min], list[i]
    return (list)

# DRIVER CODE FOR TESTING THE ALGORITHM.
list = [3, 5, 0, 9, 1, 6, 2, 8, 7, 4]
print(selection_sort(list))