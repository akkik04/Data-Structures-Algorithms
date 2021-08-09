# TWO DISTINCT ELEMENTS EDABIT SOLUTION:

def return_unique(lst):
  
  # creating a list to add the distinct elements into.
  l = []
  
  # creating a for-loop to iterate for the elements in the list.
  for i in lst:
    
    # creating a nested if-statement to check for the element being present only once.
    if lst.count(i) == 1:
      
      # code to append the element that is present only once into the list.
      l.append(i)
      
  # returning the list with the two distinct elements.
  return l
