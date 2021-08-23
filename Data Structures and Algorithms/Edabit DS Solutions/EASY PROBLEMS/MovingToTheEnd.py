# MOVING TO THE END EDABIT SOLUTION:

def move_to_end(lst, el):
  
  # creating a for-loop to iterate for the elements in the list.
  for i in lst:
    
    # creating a nested if-statement to check if the elements in the list are the desired element.
    if i == el:
      
      # removing and appending the desired element to the end if the condition is met.
      lst.remove(i)
      lst.append(i)
  
  # returning the modified list.
  return lst
  
