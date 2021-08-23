# STAND IN LINE EDABIT SOLUTION:

def next_in_line(lst, num):
  
  # creating an if-statement to check for an empty list.
  if len(lst) == 0:
    
    # returning a comment regarding the empty list to the user.
    return "No list has been selected"
  
  else:
    
    # removing the first element and adding the desired element.
    lst.remove(lst[0])
    lst.append(num)
  
  # returning the modified list.
  return lst
