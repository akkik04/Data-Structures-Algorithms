# LIST OPERATION EDABIT SOLUTION:

def list_operation(x, y, n):
  
  # creating a list to append the elements that are divisible by 'n'.
  l = []
  
  # creating a for-loop to iterate from the x to y (both inclusive).
  for i in range(x, y + 1):
    
    # creating a nested if-statement to check for the element's divisibility by 'n'.
    if i % n == 0:
      
      # code to append the element into the created list if the element is divisible by 'n'.
      l.append(i)
  
  # returning the list.
  return l
