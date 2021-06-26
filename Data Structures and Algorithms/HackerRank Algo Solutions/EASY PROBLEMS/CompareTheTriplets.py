# COMPARE THE TRIPLETS HACKERRANK SOLUTION:

# creating a function to compare the indexes of each array.
def compareTriplets(a, b):

    # declaring variables to store the score of each person.
    alice_score = 0
    bob_score = 0

    # creating a for-loop to iterate for the length of the 'a' array.
    for i in range(len(a)):
        
        # creating an if-statement to compare each array's indexes.
        if a[i] > b[i]:

            # incrementing alice's score if conditions are met.
            alice_score += 1

        elif a[i] < b[i]:

            # incrementing bob's score if conditions are met.
            bob_score += 1
    
    # returning alice's and bob's score.
    return alice_score, bob_score

# receiving input.
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

# printing the final output, which indicates each individual's score.
result = compareTriplets(a, b)
print(result)