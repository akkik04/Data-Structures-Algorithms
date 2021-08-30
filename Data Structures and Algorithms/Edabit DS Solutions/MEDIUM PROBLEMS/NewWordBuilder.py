# NEW WORD BUILDER EDABIT SOLUTION:

def word_builder(ltr, pos):
  
  # creating a list to append the elements.
  l = []
  
  # creating a for-loop to iterate for the positions in the list.
  for i in pos:
    
    # code to append the appropriate position's element from the other list.
    l.append(ltr[i])
  
  # returning the string version of the list.
  return "".join(l)
