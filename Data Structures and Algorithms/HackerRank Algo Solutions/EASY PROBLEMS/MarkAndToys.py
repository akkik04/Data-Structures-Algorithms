# MARK AND TOYS HACKERRANK SOLUTION:

# creating a function to calculate the maximum number of toys bought.
def maximumToys(prices, k):

    # creating a variable to store the number of toys.
    num_toys = 0

    # sorting the initial prices array.
    prices = sorted(prices)

    # creating a for-loop to iterate for the length of the prices array.
    for i in range(len(prices)):

        # calculating which toys are affordable.
        k = k - prices[i]

        # creating a nested if-statement to break if the toy is not affordable.
        if k <= 0:

            break
        
        # code to increase the count of the number of toys.
        num_toys += 1

    # returning the value for the number of toys that are possible to purchase.
    return num_toys

# receiving input.
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
prices = list(map(int, input().rstrip().split()))

# printing the final output, which indicates the maximum number of toys bought.
result = maximumToys(prices, k)
print(result)