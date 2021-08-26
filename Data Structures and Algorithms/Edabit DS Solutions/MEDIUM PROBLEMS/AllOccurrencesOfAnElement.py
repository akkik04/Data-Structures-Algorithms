# ALL OCCURRENCES OF AN ELEMENT IN A LIST EDABIT SOLUTION:

def get_indices(lst, el):
  
  # creating a list to append the indexes of the desired element.
  l = []
  
  # creating a for-loop using enumerate to access the index of the desired element.
  for idx, num in enumerate(lst):
    
    # creating a nested if-statement to check if the element is present within the list.
    if num == el:
      
      # appending the index at which the element is present, if the condition is met.
      l.append(idx)
  
  # returning the list with the indexes at which the element is present.
  return l
