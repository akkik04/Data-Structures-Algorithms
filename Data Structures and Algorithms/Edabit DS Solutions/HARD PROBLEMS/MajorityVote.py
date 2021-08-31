# MAJORITY VOTE EDABIT SOLUTION:

def majority_vote(lst):
  
  # creating a for-loop to iterate for the elements in the list.
  for i in lst:
    
    # creating a nested if-statement to check for the majority element.
    if lst.count(i) > len(lst) / 2:
      
      # returning the majority element if the condition is met.
      return i
  
  # returning 'None' if there is no majority element.
  return None
