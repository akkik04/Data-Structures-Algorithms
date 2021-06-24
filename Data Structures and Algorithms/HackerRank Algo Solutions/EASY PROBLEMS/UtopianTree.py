# UTOPIAN TREE HACKERRANK SOLUTION:

# creating a function to calculate the height of the tree at the given cycle.
def utopianTree(n):

    # creating a variable to store the intial value of the height.
    height = 1

    # creating a for-loop to iterate till the cycle.
    for i in range(n):

        # creating an if-statement to apply the appropriate arithmetic changes to the height depending on the season.
        if i % 2 == 0:
            height *= 2

        else: 
            height += 1

    # returning the value of the height.
    return height

# receiving input.
t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

# code to print the final output, which indicates the height of the tree at the given cycle.
result = utopianTree(n)
print(result)