# FIND THE SHARED LETTERS BETWEEN TWO STRINGS EDABIT SOLUTION:

def shared_letters(a, b):
  
  # creating a variable to hold the shared letters.
  common = ""
  
  # creating a for-loop to iterate for the lowercase version of string 'a'.
  for i in a.lower():
    
    # creating a nested if-statement to check if any of the letters from string 'a' are in lowercase string 'b'.
    if i in b.lower():
      
      # adding the common letter into the variable to store it.
      common += i
  
  # returning the shared letters after sorting and applying appropropriate changes to remove the same letter twice (using set()).
  return "".join(sorted(set(common)))
