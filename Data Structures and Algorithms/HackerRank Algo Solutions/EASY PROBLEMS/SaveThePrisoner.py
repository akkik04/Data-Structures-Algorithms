# SAVE THE PRISONER HACKERRANK SOLUTION:

# creating a function to save the prisoner from the faulty candy.
def saveThePrisoner(n, m, s):

    # finding the remainder.
    x = m % n

    # creating an if-statement to check which individual is affected by the bad candy. 
    if ((x + s - 1) % n == 0):
        return x
    
    else:
        return (x + s - 1)

# receiving input.
t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    s = int(first_multiple_input[2])

# printing the final output, which indicates which chair is getting the faulty candy.
result = saveThePrisoner(n, m, s)
print(result)