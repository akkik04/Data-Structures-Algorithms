# CLUB ENTRY EDABIT SOLUTION:

def club_entry(word):

    # creating a for-loop to iterate for the characters in the word.
    for i in range(len(word) - 1):

        # creating a nested if-statement to check for the same character being repeated twice.
        if word[i] == word[i + 1]:

            # returning the appropriate value after finding the number of the alphabet and multiplying it by four.
            return (ord(word[i]) - 96) * 4