# BEAUTIFUL DAYS AT THE MOVIES HACKERRANK SOLUTION:

# creating a function to calculate the number of beautiful days.
def beautifulDays(i, j, k):

    # creating a variable that stores the number of beautiful days.
    count = 0

    # creating a for-loop to iterate for the list.
    for x in range(i, j + 1):

        # determining the reverse of the number.
        rev = int(str(x)[::-1])

        # creating an if-statement to check if the difference between the number and it's reversed is evenly divisible by 'k'.
        if abs(x- rev) % k == 0:
            count += 1
    
    # returning the value for the number of beautiful days.
    return count

# receiving input.
first_multiple_input = input().rstrip().split()
i = int(first_multiple_input[0])
j = int(first_multiple_input[1])
k = int(first_multiple_input[2])

# printing the final output, which indicates the number of beautiful days.
result = beautifulDays(i, j, k)
print(result)