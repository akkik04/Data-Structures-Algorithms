# RECURSIVE ARRAY SUM EDABIT SOLUTION:

def sum_recursively(lst):

    # creating an if-statement to check for an empty list.
    if len(lst) == 0:

        # returning '0' if the list is empty.
        return 0
    
    # calling the recursive function.
    return lst[0] + sum_recursively(lst[1:])