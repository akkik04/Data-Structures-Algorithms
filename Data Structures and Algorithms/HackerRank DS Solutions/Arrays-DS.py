# ARRAYS-DS HACKERRANK SOLUTION:

# creating a function to reverse the given array.
def reverseArray(arr):

    # code to reverse the given array.
    reversed_array = arr[::-1]

    # returning the reversed array.
    return reversed_array

# receiving input.
arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the reversed form of the original array.
result = reverseArray(arr)
print(result)