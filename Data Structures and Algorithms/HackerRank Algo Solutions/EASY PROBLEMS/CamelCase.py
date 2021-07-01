# CAMEL CASE HACKERRANK SOLUTION:

# creating a function to calculate the number of words in a given string.
def camelcase(s):

    # creating a variable to track the number of words, the variable is initialized to 1 to account for the first word.
    word_count = 1

    # creating a for-loop to iterate for the length of the string.
    for i in range(len(s)):
        
        # creating a nested if-statement to increment the word count if certain conditions are met.
        if s[i] == s[i].upper():

            # incrementing the word count if the conditions are met.
            word_count += 1
    
    # returning the number of words in the string.
    return word_count

# receiving input.
s = input()

# code to print the final output, which indicates the number of words in the string.
result = camelcase(s)
print(result)