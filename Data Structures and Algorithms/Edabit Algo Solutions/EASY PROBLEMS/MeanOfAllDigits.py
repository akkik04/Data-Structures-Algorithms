# FIND THE MEAN OF ALL DIGITS EDABIT SOLUTION:

# creating a function to solve the problem.
def mean(num):
   
  # returning the mean of all the digits after appropriate conversions.
  return sum(map(int, str(num))) / len(str(num))
