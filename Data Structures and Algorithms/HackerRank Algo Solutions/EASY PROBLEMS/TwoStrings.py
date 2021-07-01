# TWO STRINGS HACKERRANK SOLUTION:

# creating a function to find a common substring between two strings.
def twoStrings(s1, s2):

    # creating a for-loop to iterate for the first string.
    for i in s1:

        # creating a nested if-statement to determine if a substring exists between both strings.
        if i in s2:

            # returning 'YES' if there is a common substring.
            return 'YES'
    
    # returning 'NO' if there is no common substring.
    return 'NO'

# receiving input.
q = int(input().strip())

for q_itr in range(q):
    s1 = input()

    s2 = input()

# code to print the final output, which indicates if both of the strings share a common substring.
result = twoStrings(s1, s2)
print(result)