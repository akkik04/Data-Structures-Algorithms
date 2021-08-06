# RETURN LAST ITEM EDABIT SOLUTION:

# creating a function to solve the problem.
def last_ind(lst):
  
  # creating a nested if-statement to check for an empty list.
  if len(lst) != 0:
    
    # returning the last item of the list or string if the condition is met.
    return lst[-1]
  
  # returning None if the list or string is empty.
  return None
