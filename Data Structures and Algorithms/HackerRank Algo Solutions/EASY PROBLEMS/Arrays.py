# ARRAYS-DS HACKERANK SOLUTION:

# creating a function to reverse the array.
def reverseArray(arr):

    # reversing the array.
    reversed = arr[::-1]
    
    # returning the reversed array.
    return reversed

# receiving input.
arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))

# printing the output.
print(reverseArray(arr))