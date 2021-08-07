# FIND THE ODD INTEGER EDABIT SOLUTION:

def find_odd(lst):
  
  # creating a for-loop to iterate for the elements in the given list.
  for i in lst:
    
    # creating a nested if-statement to check for the odd count of an element.
    if lst.count(i) % 2 != 0:
      
      # returning the element that satisfies the condition.
      return i
