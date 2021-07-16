# SALES BY MATCH HACKERRANK SOLUTION:

# creating a function to determine the number of pairs.
def sockMerchant(n, ar):

    # creating a variable to keep track of the pairs.
    pair_count = 0

    # creating a for-loop to iterate through the set of elements.
    for i in set(ar):

        # incrementing the count by each amount of pairs found.
        pair_count += ar.count(i) // 2

    # returning the count of pairs.
    return pair_count  

# receiving input.
n = int(input().strip())
ar = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the number of pairs.
result = sockMerchant(n, ar)
print(result)