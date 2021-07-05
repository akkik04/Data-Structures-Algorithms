# ALTERNATING CHARACTERS HACKERRANK SOLUTION:

# creating a function to calculate the required amount of deletions on the string.
def alternatingCharacters(s):

    # declaring a variable to store the value for the number of deletions.
    count = 0

    # creating a for-loop to iterate for the array.
    for i in range(len(s) - 1):

        # creating a nested if-statement to check if adjacent elements are the same.
        if s[i] == s[i + 1]:

            # incrementing the count for deletions if any adjacent elements are the same.
            count += 1
    
    # returning the value for the required amount of deletions.
    return count 

# receiving input.
q = int(input().strip())
for q_itr in range(q):
    s = input()

# code to print the final output, which indicates the required amount of deletions.
result = alternatingCharacters(s)
print(result)