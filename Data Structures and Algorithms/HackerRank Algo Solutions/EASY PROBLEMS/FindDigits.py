# FIND DIGITS HACKER-RANK SOLUTION:

# creating a function to determine the number of divisors.
def findDigits(n):

    # creating a variable to track the amount of divisors.
    divisor_count = 0

    # creating a for-loop to iterate for the length of the string 'n'.
    for i in str(n):

        # creating a nested if-statement to check if the digit in 'n' is a divisor.
        if int(i) != 0 and n % int(i) == 0:

            # incrementing the divisor count if the condition for a divisor is met.
            divisor_count += 1
    
    # returning the value of the divisor count.
    return divisor_count

# receiving input.      
t = int(input().strip())
for t_itr in range(t):

    n = int(input().strip())

# printing the final output, which indicates the number of divisors.
result = findDigits(n)
print(result)