# DELETE OCCURRENCES OF EXTRA ELEMENTS IN A LIST EDABIT SOLUTION:

def delete_occurrences(lst, num):
  
  # creating a list to append the elements that do not appear more than the desired amount.
  l = []
  
  # creating a for-loop to iterate for the elements in the list.
  for i in lst:
    
    # creating a nested if-statement to check if the count of the element is less than the desired amount.
    if lst.count(i) < num:
      
      # code to append the element if the count is less than the desired amount.
      l.append(i)
  
  # returning the list.
  return l

