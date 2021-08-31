# SHARING IS CARING EDABIT SOLUTION:

def show_the_love(lst):

    # creating a variable to store the index of the minimum number in the list.
    min_index = lst.index(min(lst))

    # creating a for-loop to iterate for the elements in the list.
    for i in range(len(lst)):

        # creating a nested if-statement to make sure that we avoid changing the minimum value.
        if i != min_index:

            # code to add 25% of the element to the minimum value.
            lst[min_index] += (lst[i] * 0.25)

            # code to decrease the 25% from the initial element because it was transferred to the minimum value.
            lst[i] -= (lst[i] * 0.25)
    
    # returning the modified list.
    return lst