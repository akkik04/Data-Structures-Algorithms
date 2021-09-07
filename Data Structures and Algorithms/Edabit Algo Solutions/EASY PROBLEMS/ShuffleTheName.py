# SHUFFLE THE NAME EDABIT SOLUTION:

def name_shuffle(txt):
  
  # code to split the name into a list consisting of the first name and last name.
  txt = txt.split()
  
  # creating a for-loop to iterate for the elements in the list (first and last names).
  for i in range(len(txt) - 1):
    
    # code to perform the swapping process of the names.
    txt[i], txt[i + 1] = txt[i + 1], txt[i]
  
  # returning the string version of the full name after the shuffling.
  return " ".join(txt)
