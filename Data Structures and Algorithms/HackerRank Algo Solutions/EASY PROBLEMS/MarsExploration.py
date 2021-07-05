# MARS EXPLORATION HACKERRANK SOLUTION:

# creating a function to calculate the number of letters changed during transmission.
def marsExploration(s):
    
    # declaring a variable to track the count of letters switched. 
    num_switched = 0

    # code to determine how the original signal should be.
    orig_string = "SOS" * (len(s) // 3)

    # creating a for-loop to iterate for the length of the letters in the string.
    for i in range(len(s)):

        # creating a nested if-statement to increment the count if letters do not match between the original and transmitted strings.
        if orig_string[i] != s[i]:
            
            # incrementing the count if certain conditions are met.
            num_switched += 1
    
    # returning the value for the number of letters switched.
    return num_switched

# receiving input.
s = input()

# code to print the final output, which indicates the number of letters switched during transmission.
result = marsExploration(s)
print(result)