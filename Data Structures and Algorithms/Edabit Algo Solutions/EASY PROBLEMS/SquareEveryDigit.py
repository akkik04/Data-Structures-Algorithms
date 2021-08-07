# SQUARE EVERY DIGIT EDABIT SOLUTION:

def square_digits(n):

    # creating a string to add the squares into.
    l = " "

    # creating a for-loop to iterate for the string version of 'n'.
    for i in str(n):

        # code to add the string version of the square into the created string.
        l += str(int(i) ** 2)

    # returning the integer version of the string.
    return int(l)
