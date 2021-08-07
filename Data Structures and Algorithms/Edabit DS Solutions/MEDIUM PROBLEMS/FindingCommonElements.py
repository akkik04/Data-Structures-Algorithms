# FINDING COMMON ELEMENTS EDABIT SOLUTION:

def common_elements(lst1, lst2):
   
  # creating a list to append the common elements into.
  l = []
  
  # creating a for-loop to iterate for the elements in the first list.
  for i in lst1:
    
     # creating a nested if-statement to check for the same element in the second list, while making sure we do not append the same element twice.
    if i not in l and i in lst2:
      
       # code to append the element if the condition is met.
      l.append(i)
  
  # returning the list with the common elements.
  return l
