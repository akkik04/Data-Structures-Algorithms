# LIST OF MULTIPLES EDABIT SOLUTION:

def list_of_multiples(num, length):
  
  # creating a list to append the multiples into.
  l = []
  
  # creating a for-loop to iterate until the length.
  for i in range(1, length + 1):
    
    # code to multiply the counter 'i' by the number each time to find the multiples.
    l.append(i * num)
  
  # returning the list with the multiples.
  return l
