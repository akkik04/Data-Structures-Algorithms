# AKSHITH K 
# LINEAR SEARCH IMPLEMENTED IN PYTHON WITH USER INPUT.

# creating a function to search for the desired element in the array.
def linear_search(arr, desired_element):

    # creating a for-loop to iterate for the elements in the array.
    for i in range(len(arr)):
        
        # creating a nested if-statement to check if the element is found at an index in the array.
        if arr[i] == desired_element:

            # returning the value of the index if desired element is present at it. 
            return 'The element is present at index ' + str(i)

    # returning 'None' if the element is not found in the array.
    return None

# receiving input for the array and desired element.
arr = list(map(int, input().rstrip().split()))
desired_element = int(input())

# code to print the final output, which indicates if the element is found at an index.
result = linear_search(arr, desired_element)
print(result)
