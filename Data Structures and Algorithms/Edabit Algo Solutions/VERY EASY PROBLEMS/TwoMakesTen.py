# TWO MAKES TEN EDABIT SOLUTION:

# creating a function to solve the problem.
def makes10(a, b):
  
  # creating an if-statement to check if the arguments pass the test.
  if a + b == 10 or a / 10 == 1 or b / 10 == 1:
     
      # returning 'True' if the condition is met.
    return True
  
  # creating an else statement to handle the arguments not meeting the conditions.
  else:
    
    # returning 'False' if the condition is not met.
    return False
