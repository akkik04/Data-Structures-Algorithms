# SIMPLE ARRAY SUM HACKERRANK SOLUTION:

# creating a function to calculate the sum of the integers in an array.
def simpleArraySum(ar):

    # finding the sum of all indexes using the built-in 'sum' function.
    x = sum(ar)

    # returning the value of sum.
    return x

# receiving input.
ar_count = int(input().strip())
ar = list(map(int, input().rstrip().split()))

# printing the final output, which indicates the sum of the integers in the array.
result = simpleArraySum(ar)
print(result)