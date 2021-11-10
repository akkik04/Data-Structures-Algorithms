# INTEGER DIGITS COUNT EDABIT SOLUTION:

def count(n):
  
  # creating a variable to store the count of integers.
  count = 0
  
  # creating a for-loop to iterate for the string version of the given integer.
  for i in str(n):
    
    # creating a nested if-statement to check if the element is a digit.
    if i.isdigit():
      
      # code to increment the count if the condition is met.
      count += 1
  
  # returning the value of the number of digits.
  return count
