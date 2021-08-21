# FACE INTERVAL EDABIT SOLUTION:

def face_interval(num):
  
  # creating an if statement to check if the given input is not a list.
  if type(num) != list:
    
    return ":/"
  
  # creating an if-statement to check if the max - min of the list is in the list itself.
  if (max(num) - min(num)) in num:
    
    # returning a happy face if the interval of the list is present within the list itself.
    return ":)"
  
  # returning a sad face if the interval of the list is not present in the list itself.
  return ":("
