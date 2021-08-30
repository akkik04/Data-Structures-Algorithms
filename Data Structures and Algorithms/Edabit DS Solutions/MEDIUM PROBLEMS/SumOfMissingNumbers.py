# SUM OF MISSING NUMBERS EDABIT SOLUTION:

def sum_missing_numbers(lst):
  
  # creating a variable to track the sum of the missing numbers.
  summ = 0
  
  # creating a for-loop to iterate from the minimum to the maximum of the list.
  for i in range(min(lst), max(lst) + 1):
    
    # creating a nested if-statement to check for an element not being present within the desired range.
    if i not in lst:
      
      # code to add the missing element to the sum of the missing numbers.
      summ += i
  
  # returning the sum of the missing elements.
  return summ
