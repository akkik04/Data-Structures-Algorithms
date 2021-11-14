# LAST DIGIT ULTIMATE EDABIT SOLUTION:

def last_dig(a, b, c):
  
  # creating a variable to store the product of 'a' and 'b'.
  product_ab = a * b
  
  # creating an if-statement to check for the last digits being similar between the product of 'a' and 'b' to 'c'.
  if (product_ab % 10) == (c % 10):
    
    # returning 'True' if the condition is met.
    return True
  
  # returning 'False' if the condition is not met.
  return False
