# SUM OF EVENLY DIVISIBLE NUMBERS FROM A RANGE EDABIT SOLUTION:

def evenly_divisible(a, b, c):
  
  # creating a variable to store the sum.
  summ = 0
  
  # creating a for-loop to iterate to-and-from the desired values.
  for i in range(a, b + 1):
    
    # creating a nested if-statement to check for an evenly divisible number.
    if i % c == 0:
      
      # code to add the number to the sum if the conditions are met.
      summ +=i 
  
  # returning the value for the sum.
  return summ
