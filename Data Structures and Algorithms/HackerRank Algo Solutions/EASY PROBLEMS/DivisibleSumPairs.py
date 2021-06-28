# DIVISIBLE SUM PAIRS HACKERRANK SOLUTION:

# creating a function to find the number of pairs that meet the requirements.
def divisibleSumPairs(n, k, ar):

    # creating a variable to store the count of pairs that satisfy the requirements.
    pair_count = 0

    # creating two for-loops to iterate and find pairs.
    for i in range(0, len(ar)):

        for j in range(i + 1, len(ar)):
            
            # creating a nested if-statement to increment the count of pairs if the sum of the pair is evenly divisible by 'k'.
            if ((ar[i] + ar[j]) % k) == 0:

                # incrementing the count for the pairs if the conditions are met.
                pair_count += 1
    
    # returning the value for the number of pairs that met the requirements.
    return pair_count

# receiving input.
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
ar = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the number of pairs that satisfy the requirements.
result = divisibleSumPairs(n, k, ar)
print(result)