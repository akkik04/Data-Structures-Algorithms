# ICE CREAM PARLOR HACKERRANK SOLUTION:

# creating a function to find the indices of the appropriate prices to buy.
def icecreamParlor(m, arr):

    # creating a for-loop to iterate for the length of the elements in the array.
    for i in range(len(arr)):

        # creating a nested for-loop to iterate for finding elements that satisfy the requirements.
        for j in range(i + 1, len(arr)):

            # creating a nested if-statement to return the indices of the prices if conditions are met.
            if arr[i] + arr[j] == m:

                return i + 1, j + 1
                
                break

# receiving input.
t = int(input().strip())
for t_itr in range(t):
    m = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the indices of the appropriate prices of ice cream to purchase.
result = icecreamParlor(m, arr)
print(result)