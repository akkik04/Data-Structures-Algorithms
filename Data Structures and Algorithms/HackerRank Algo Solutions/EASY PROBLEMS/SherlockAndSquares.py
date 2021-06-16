# SHERLOCK AND SQUARES HACKERANK SOLUTION:

# importing the math module.
import math

# creating a function to calculate the number of perfect squares within a range. 
def squares(a, b):

    # returning the arithmetic calculation.
    return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1

# receiving input.
q = int(input().strip())
for q_itr in range(q):

    first_multiple_input = input().rstrip().split()
    a = int(first_multiple_input[0])
    b = int(first_multiple_input[1])

# storing the returned value from the function in the 'result' variable.
result = squares(a, b)

# printing the final output, which indicates the number of square integers.
print(result)