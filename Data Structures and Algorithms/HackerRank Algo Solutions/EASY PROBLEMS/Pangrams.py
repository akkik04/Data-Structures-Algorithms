# PANGRAMS HACKERRANK SOLUTION:

# creating a function to determine if a string is a pangram.
def pangrams(s):

    # declaring a variable to store the letters of the alphabet.s
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    # declaring a variable to store the count.
    pangram_count = 0

    # creating a for-loop to iterate for all the letters in the alphabet.
    for i in alphabets:

        # creating a nested if-statement to increment the count if the letter is found or keep it the same if it is not found.
        if i not in s.lower():
            pangram_count = pangram_count
        
        else:

            pangram_count += 1
    
    # creating an if-statement to return if the string is a pangram.
    if pangram_count == 26:
        return 'pangram'
    
    else:
        return 'not pangram'

# receiving input.
s = input()

# printing the final output, which indicates if the string is a pangram.
result = pangrams(s)
print(result)