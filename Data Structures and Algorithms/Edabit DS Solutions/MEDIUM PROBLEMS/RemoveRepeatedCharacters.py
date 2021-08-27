# REMOVE REPEATED CHARACTERS EDABIT SOLUTION:

def unrepeated(txt):
  
  # creating a list to append the characters that don't repeat.
  l = []
  
  # creating a for-loop to iterate for the characters in the string.
  for i in txt:
    
    # creating a nested if-statement to check if the character is not already present within the list.
    if i not in l:
      
      # code to append the character that is not already present.
      l.append(i)
  
  # returning the string form of the list, with all repeated characters removed.
  return "".join(l)
