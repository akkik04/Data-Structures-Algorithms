# A VERY BIG SUM HACKERRANK SOLUTION:

# creating a function to calculate the sum.
def aVeryBigSum(ar):

    # declaring a variable to store the value for the sum.
    sum = 0

    # creating a for-loop to iterate for the elements in the array.
    for i in range(len(ar)):

        # code to add up all the elements in the array.
        sum += ar[i]
    
    # returning the value for the sum of all the elements in the array.
    return sum

# receiving input.
ar_count = int(input().strip())
ar = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the sum of all the elements in the array.
result = aVeryBigSum(ar)
print(result)