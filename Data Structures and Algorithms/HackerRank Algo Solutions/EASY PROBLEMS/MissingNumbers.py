# MISSING NUMBERS HACKERRANK SOLUTION:

# creating a function to find the missing elements when comparing both arrays.
def missingNumbers(arr1, arr2):

    # creating a list to append the missing elements.
    missing_numbers = []

    # creating a for-loop to iterate for the elements in the second array.
    for i in arr2:

        # creating an if-statement to check if the element exists within the first array.
        if i in arr1:

            # code to remove the similar element if the condition is met.
            arr1.remove(i)
        
        # code to handle if the element is not found in both arrays.
        else:

            # appending the missing number from both arrays if the condition is met.
            missing_numbers.append(i)
    
    # returning the appended list of missing numbers, while sorting it.
    return sorted(missing_numbers)

# receiving input.
n = int(input().strip())
arr1 = list(map(int, input().rstrip().split()))
m = int(input().strip())
arr2 = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the missing elements in both arrays.
result = missingNumbers(arr1, arr2)
print(result)