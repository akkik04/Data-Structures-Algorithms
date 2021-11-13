# IS THE NUMBER A REPDIGIT EDABIT SOLUTION:

def is_repdigit(num):
  
  # creating an if-statement to check for the number being a repdigit.
  if num > 0 and str(num) == str(num)[0] * len(str(num)):
    
    # returning 'True' if the neccessary conditions are met.
    return True
  
  # returning 'False' if the conditions are not met.
  return False
