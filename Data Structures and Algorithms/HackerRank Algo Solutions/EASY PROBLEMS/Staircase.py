# STAIRCASE HACKERRANK SOLUTION:

# creating a function to print the staircase.
def staircase(n):

    # creating a for-loop to print the staircase for the indicated amount of rows.
    for i in range(1, n + 1):
        
        # printing the staircase.
        print(str('#' * i).rjust(n))

# receiving input.
n = int(input().strip())

# calling the function to print the final output, which is the staircase for the desired amount of rows.
result = staircase(n)