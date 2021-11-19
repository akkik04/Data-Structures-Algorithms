# FIRST TWO CODING BAT SOLUTION:

def first_two(str):
  
  # creating an if-statement to check if the entire string is less than two.
  if len(str) <= 2:
    
    # returning the string, if the condition is met.
    return str
  
  else:
    
    # returning the first two letters of the string.
    return str[:2]
