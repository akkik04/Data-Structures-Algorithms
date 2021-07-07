# HACKERRANK IN A STRING! HACKERRANK SOLUTION:

def hackerrankInString(s):

    # declaring the string to look for.
    string = 'hackerrank'

    # creating a variable to store the length of the desired string.
    x = len(string)

    # declaring a counter.
    i = 0

    # creating a for-loop to iterate for the inputted string.
    for char in s:  

        # creating a nested if-statement to increment the count if indices match with both strings.
        if char in string[i]:

            # incrementing the count if certain conditions are met.
            i += 1

            # creating an if-statement to check if the count is equal to the length of the desired string.
            if i == x:

                # returning 'YES' if the count matches to the length of the string, indicating 'hackerrank' was found.
                return 'YES'
    
    # returning 'NO' if 'hackerrank' is not found.
    return 'NO'

# receiving input.
q = int(input().strip())
for q_itr in range(q):
    s = input()

# code to print the final output, which indicates if 'hackerrank' is present within the string.
result = hackerrankInString(s)
print(result)