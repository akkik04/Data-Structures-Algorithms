# PAIRS HACKERRANK SOLUTION:

# creating a function to find the number of pairs with difference of 'k'.
def pairs(k, arr):

    # creating a variable to track the count of pairs.
    pair_count = 0

    # creating a set of iterable elements from the given array.
    arr = set(arr)

    # creating a for-loop to iterate for the elements in the set
    for i in arr:

        # creating a nested if-statement to check if a pair with a difference of 'k' is found.
        if i + k in arr:

            # code to increment the pair count if the condition is met.
            pair_count += 1
    
    # returning the count of pairs that meet the requirements.
    return pair_count

# receiving input.
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the number of pairs with a difference of 'k'.
result = pairs(k, arr)
print(result)