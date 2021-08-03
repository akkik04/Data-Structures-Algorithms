# COUNT ONES IN BINARY REPRESENTATION OF INTEGER EDABIT SOLUTION:

# creating a function to solve the problem.
def count_ones(num):

    # creating a variable to keep track of the count of number 1's.
    count = 0

    # creating a variable to hold the binary representation of 'num'.
    bin_rep = bin(num)

    # creating a for-loop to iterate for the string version of the binary representation.
    for i in str(bin_rep):

        # creating a nested if-statement to check if the desired number is met.
        if bin_rep.count(i) == "1":

            # code to increment the count if the condition is met.
            count += 1

    # returning the value of the count.
    return count