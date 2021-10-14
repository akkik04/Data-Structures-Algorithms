# RADIANS TO DEGREES EDABIT SOLUTION:

# importing the neccessary math module.
import math

# creating a function to solve the problem.
def radians_to_degrees(rad):
  
  # applying the appropriate conversion.
  degrees = (rad * 180) / math.pi
  degrees = round(degrees, 1)
  
  return degrees
  
  
