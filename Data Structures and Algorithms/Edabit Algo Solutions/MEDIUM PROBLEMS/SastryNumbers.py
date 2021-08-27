# SASTRY NUMBERS EDABIT SOLUTION:

# importing the math module to access the functions.
import math

def is_sastry(n):
  
  # finding the numbers successor.
  successor = n + 1
  
  # concatenating the given number and its successor.
  n = int(str(n) + str(successor))
  
  # finding the root of the concatenated number to use in the perfect square process.
  root = math.sqrt(n)
  
  # creating an if-statement to check if the concatenated number is a perfect square. 
  if int(root + 0.5) ** 2 == n:
    
    # returning 'True' if the number is a perfect square.
    return True
  
  # returning 'False' if the number is not a perfect square.
  return False
