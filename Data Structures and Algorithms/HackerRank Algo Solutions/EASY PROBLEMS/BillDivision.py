# BILL DIVISION HACKERRANK SOLUTION: 

# creating a function to determine the bill's status.
def bonAppetit(bill, k, b):

    # creating a variable to track the total.
    total = 0

    # creating a for-loop to iterate for the length of the bill.
    for i in range(0, len(bill)):

        # code to sum up all the values in the bill list.
        total = total + bill[i]
    
    # applying the appropriate change to the bill. 
    total = (total - bill[k]) / 2

    # creating an if-statement to check if the individual was overcharged.
    if b > total:

        return b - total

    else:
        
        return 'Bon Appetit'

# receiving input.
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())

# storing the returned value from the 
result = bonAppetit(bill, k, b)

# printing the final output, which indicates the bill's status.
print(result)