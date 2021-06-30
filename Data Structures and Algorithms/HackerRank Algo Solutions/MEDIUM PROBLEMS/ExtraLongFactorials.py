# EXTRA LONG FACTORIALS HACKKERANK SOLUTION:

# creating a function to calculate the factorial of a number. 
def extraLongFactorials(n):

    # declaring a variable to store the initial value of the factorial.
    x = 1

    # creating a while-loop to iterate for the time that 'n' is not 1.
    while n != 1:

        # applying the appropriate arithmetic calculation for a factorial.
        x *= n

        # decreasing the count of 'n'.
        n -= 1
    
    # printing the final output, which indicates the factorial of the number.
    print(x)

# receiving input.
n = int(input().strip())

# calling the function to print the final output to the user, which indicates the factorial of the desired number.
extraLongFactorials(n)