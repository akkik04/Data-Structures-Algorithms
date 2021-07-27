# BEAUTIFUL TRIPLETS HACKERRANK SOLUTION:

# creating a function to return the number of beautiful triplets.
def beautifulTriplets(d, arr):

    # creating a variable to track the count.
    count = 0

    # creating a for-loop to iterate for the length of the array.
    for i in range(len(arr)):

        # creating a nested for-loop to iterate based on the first loop.    
        for j in range(i + 1, len(arr)):
            
            # creating a nested if-statement to check if the condition is met between elements i and j.
            if arr[j] - arr[i] == d:

                # creating a nested for-loop to iterate based on the second loop.
                for k in range(j + 1, len(arr)):

                    # creating a nested if-statement to check if the condition is met between elements j and k.
                    if arr[k] - arr[j] == d:

                        # code to increment the count variable if the condition is met.
                        count += 1
                        break
    
    # returning the value of the count.
    return count

# receiving input.
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the number of beautiful triplets.
result = beautifulTriplets(d, arr)
print(result)