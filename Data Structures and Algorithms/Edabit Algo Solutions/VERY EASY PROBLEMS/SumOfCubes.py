# SUM OF CUBES EDABIT SOLUTION:

# creating a function to solve the problem.
def sum_cubes(n):

    # initializing a variable to keep track of the sum.
    sum = 0

    # creating a for-loop to iterate for the numbers between 'n'.
    for i in range(1, n + 1):

        # code to increment the sum by each number cubed for every iteration.
        sum += i ** 3

    # returning the value of the sum.
    return sum 