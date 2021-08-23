# FILTER OUT STRINGS FROM AN ARRAY EDABIT SOLUTION:

def filter_list(lst):
  
  # creating a list to append the non-string elements into.
  l = []
  
  # creating a for-loop to iterate for all the elements in the list.
  for i in lst:
    
    # creating a nested if-statement to check if the element is a number.
    if type(i) == int:
      
      # if the element is a number and not a string, we append the element into the created list.
      l.append(i)
      
    else:
      
      # pass if the element is a string.
      pass
  
  # returning the list with the non-string elements seperated from the strings.
  return l
