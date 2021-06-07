# CHOCOLATE FEAST HACKER-RANK SOLUTION.

# creating a function to calculate the number of chocolates.
def chocolateFeast(n, c, m):

    # calculating the initial amount of chocolates bought using money.
    chocolates = n // c

    # creating a variable to tie the value of chocolate wrappers to the chocolates bought.
    chocolate_wrappers = chocolates

    # creating a while-loop to iterate for the amount of time that the wrappers are less than the trade-in rate.
    while chocolate_wrappers >= m:

        # calculation to determine the number of chocolates.
        chocolates += chocolate_wrappers // m
        chocolate_wrappers = chocolate_wrappers // m + chocolate_wrappers % m
    
    # returning the number of chocolates.
    return chocolates

# receiving input.

t = int(input().strip())

for t_itr in range(t):

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    result = chocolateFeast(n, c, m)

    # printing the output, which indicates the amount of chocolates eaten.
    print (result)