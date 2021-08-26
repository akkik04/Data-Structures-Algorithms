# SUM OF ODD AND EVEN NUMBERS EDABIT SOLUTION:

def sum_odd_and_even(lst):
  
  # creating a list with the format of even sum and odd sum.
  l = [0, 0]
  
  # creating a for-loop to iterate for the elements in the list.
  for i in lst:
    
    # creating a nested if-statement to check for an even number.
    if i % 2 == 0:
      
      # code to add the even number to the even sum.
      l[0] += i
      
    else:
      
      # code to add the odd number to the odd sum.
      l[1] += i
  
  # returning the list.
  return l
  
