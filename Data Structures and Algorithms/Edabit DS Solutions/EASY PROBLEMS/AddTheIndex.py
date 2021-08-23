# ADD THE INDEX EDABIT SOLUTION:

def add_indexes(lst):
  
  # creating a list to append each element's index in the list added to its value.
  l = []
  
  # creating a for-loop using 'enumerate' to get the index value and the elements actual value.
  for idx, val in enumerate(lst):
    
    # code to append the element's index added to the element's value.
    l.append(idx + val)
  
  # returning the created list.
  return l
