# JUMPING ON THE CLOUDS HACKERRANK SOLUTION:

# creating a function to print the minimum jumps required to win the game.
def jumpingOnClouds(c):

    # creating a variable to keep track of the value for the jumps in the game.
    jumps = 0

    # creating a variable to keep track of the indexes in the given array of clouds.
    i = 0

    # creating a while loop to iterate within the array.
    while i < n - 1:

        # creating an if-statement to check if it is possible to increment by two jumps.
        if i + 2 < n and c[i + 2] != 1:

            # if the condition is met, we increment the index variable by 2 and the jumps variable by 1.
            jumps += 1
            i += 2
        
        # creating an elif-statement to check if it is possible to increment by a jump.
        elif i + 1 < n and c[i + 1] != 1:

            # if the condition is met, we increment the index and jumps variables by 1.
            jumps += 1
            i += 1
    
    # returning the value of the jumps variable.
    return jumps

# receiving input.
n = int(input().strip())
c = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the minimum amount of jumps required to finish the game.
result = jumpingOnClouds(c)
print(result)