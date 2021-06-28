# PLUS MINUS HACKERRANK SOLUTION:

# creating a function to find the ratios of each type of number.
def plusMinus(arr):

    # creating variables to track the number of positive, negative and zero numbers.
    positive_count = 0
    negative_count = 0
    zero_count = 0

    # creating a for-loop to iterate for the length of the array.
    for i in range(len(arr)):

        # creating a nested if-statement to determine what count to increment based on certain conditions.
        if arr[i] > 0:
            positive_count += 1
        
        elif arr[i] < 0:
            negative_count += 1
        
        else:
            zero_count += 1
    
    # code to print the ratios of the numbers to the user, while rounding. 
    print(round(positive_count / len(arr), 4))
    print(round(negative_count / len(arr), 4))
    print(round(zero_count / len(arr), 4))

# receiving input.
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

# calling the function to output the ratios of each type of number to the user.
result = plusMinus(arr)