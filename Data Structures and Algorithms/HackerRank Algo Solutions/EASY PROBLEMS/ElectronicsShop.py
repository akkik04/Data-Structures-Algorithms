# ELECTRONICS SHOP HACKERRANK SOLUTION:

# creating a function to determine the maximum amount that can be spent on the items.
def getMoneySpent(keyboards, drives, b):

    # creating a variable to store the maximum amount of money to spend, while initializing it to "-1".
    money_to_spend = -1

    # creating a for loop to iterate through the keyboards price list.
    for i in keyboards:

        # creating a nested for-loop to iterate through the drives price list.
        for j in drives:
            
            # creating an if-statement to check if the keyboard and drive purchased is within the budget.
            if i + j <= b:

                # code to tie the variable keeping track of the expenditure to the amount found within the iterations.
                money_to_spend = max(money_to_spend, i + j)
    
    # returning the maximum amount of money that can be spent on the items.
    return money_to_spend

# receiving input.
bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))

# code to print the final output, which 
result = getMoneySpent(keyboards, drives, b)
print(result)