# INTRO TO TUTORIAL CHALLENGES HACKERRANK SOLUTION:

# creating a function to search for the desired element in an array.
def introTutorial(V, arr):

    # creating a for-loop to iterate for the elements in the array.
    for i in range(len(arr)):

        # creating a nested if-statement to determine if the desired element is found.
        if arr[i] == V:

            # code to return the index where the element is present.
            return i

    # returning 'None' if the element is not present in the array.
    return None

# receiving input.
V = int(input().strip())
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the index of the desired element.
result = introTutorial(V, arr)
print(result)