# WHICH NUMBER IS NOT LIKE THE OTHERS EDABIT SOLUTION:

# creating a function to solve the problem.
def unique(lst):
  
  # creating a for-loop to iterate for the elements in the list.
  for i in lst:
    
    # creating a nested if-statement to check for a distinct element.
    if lst.count(i) == 1:
      
      # returning the element if the condition is met.
      return i
