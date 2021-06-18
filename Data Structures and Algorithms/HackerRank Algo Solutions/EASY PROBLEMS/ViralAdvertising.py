# VIRAL ADVERTISING HACKERRANK SOLUTION:

# creating a function to calculate the cumulative likes at the given day.
def viralAdvertising(n):

    # creating a variable to store the total amount of likes. 
    total_likes = 0

    # initializing the amount of people shared to. 
    shared = 5

    # creating a for-loop to iterate until the given day.
    for i in range(0, n):

        # applying the arithmetic calculation to determine the total likes.
        likes = shared // 2
        total_likes += likes
        shared = likes * 3
    
    # returning the total likes for the given day.
    return total_likes

# receiving input.
n = int(input().strip())

# printing the final output, which indicates the cumulative likes at a given day.
result = viralAdvertising(n)
print(result)