# EQUALITY OF 3 VALUES EDABIT SOLUTION:

# creating a function to solve the problem.
def equal(a, b, c):

    # creating a list with the set function to remove the similar elements.
    l = set([a, b, c])
    
    # creating an if-statement to check if the three elements are still there, indicating the are not the same.
    if len(l) == 3:

        # returning that 0 elements are the same if the condition is met.
        return 0

    # code to return the same amount of elements using simple logic.
    else:

        # returning '4 -' the length of the list after the 'set()' function.
        return 4 - len(l)