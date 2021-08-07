# TRUE ONES, FALSE ZEROES EDABIT SOLUTION:

def integer_boolean(n):
  
  # creating a list to append the new items into.
  l = []
  
  # creating a for-loop to iterate for the elements in 'n'.
  for i in n:
    
    # code to append the boolean version of either 1 or 0 in their integer form.
    l.append(bool(int(n)))
  
  # returning the list.
  return l
