# REMOVE THE WORD EDABIT SOLUTION:

def remove_letters(letters, word):
  
  # creating a for-loop to iterate for the characters in the word.
  for i in word:
    
    # creating a nested if-statement to check if the character is present within the list.
    if i in letters:
      
      # code to remove the character if it is present within the list.
      letters.remove(i)
  
  # returning the modified version of the list.
  return letters
