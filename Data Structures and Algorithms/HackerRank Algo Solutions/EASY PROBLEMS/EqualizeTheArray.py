# EQUALIZE THE ARRAY HACKERRANK SOLUTION:

# creating a function to find the number of required deletions to equalize the array.
def equalizeArray(arr):

    # code to create a variable to track the deletions.
    deletion_count = 0

    # code to find the most common element in the array
    most_common = max(arr, key = arr.count)

    # creating a for-loop to iterate for the elements in the array.
    for i in range(len(arr)):

        # creating a nested if-statement to check if the element is not the most common.
        if arr[i] != most_common:

            # incrementing the deletion count if the condition is met.
            deletion_count += 1

    # returning the count for the number of required deletions.
    return deletion_count

# receiving input.
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the number of required deletions to equalize the array.
result = equalizeArray(arr)
print(result)