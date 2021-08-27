# CHECK THAT INPUT TYPE IS THE SAME EDABIT SOLUTION:

def compare_data(*args):
  
  # creating a list to append the input type of each argument.
  l = []
  
  # creating an if-statement to check if the arguments given are none or one.
  if len(args) == 0 or len(args) == 1:
    
    # returning 'True' if the condition is met.
    return True
  
  else:
    
    # creating a for-loop to iterate for the arguments.
    for i in args:
      
      # code to append the type of each element.
      l.append(type(i))
  
  # returning the output for the input type being the same. Using set() to make sure that only 1 element is left, indicating that the rest are the same.
  return len(set(l)) == 1
