# MINI-MAX SUM HACKKERANK SOLUTION:

# creating a function to calculate the minimum and maximum sum.
def miniMaxSum(arr):
    
    # creating a variable to store the value for the sum.
    sum_list = 0

    # code to sum up all the values in the array.
    sum_list = sum(arr)

    # code to print the minimum and maximum sum.
    print (sum_list - max(arr), sum_list - min(arr))

# receiving input.
arr = list(map(int, input().rstrip().split()))

# code to call the function to print the final output to the user, which indicates the minimum and maximum sum.
result = miniMaxSum(arr)