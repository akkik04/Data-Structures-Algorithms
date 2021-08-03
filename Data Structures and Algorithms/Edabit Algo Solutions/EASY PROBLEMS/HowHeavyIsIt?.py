# HOW HEAVY IS IT? EDABIT SOLUTION:

# importing the necessary math module.
import math

# creating a function to solve the problem.
def weight(r, h):
   
  # returning the volume in dm^3, while rounding to two decimal places.
  return round((math.pi * r ** 2 * h / 1000), 2)
