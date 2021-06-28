# COUNTING VALLEYS HACKERRANK SOLUTION:

# creating a function to calculate the number of valleys.
def countingValleys(steps, path):

    # creating variables to store the values for the valleys crossed and the current level.
    current_level = 0
    valley_count = 0

    # creating a for-loop to iterate for the length of the steps.
    for i in range(steps):

        # creating a nested if-statement to determine when the level goes up and down.
        if path[i] == 'U':
            current_level += 1
        elif path[i] == 'D':
            current_level -= 1

            # creating an if-statement to increment the count for the valleys crossed if the level is below the initialized value.
            if current_level == -1:
                valley_count += 1
    
    # returning the count for the number of valleys crossed.
    return valley_count

# receiving input.
steps = int(input().strip())
path = input()

# printing the final output, which indicates the number of valleys crossed.
result = countingValleys(steps, path)
print(result)