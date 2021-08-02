# THE 3 PROGRAMMERS PROBLEM SOLUTION:

# creating a function to solve the problem.
def programmers(one, two, three):
  
  # creating a list out of the given numbers.
  l = [one, two, three]
  
  # returning the difference between the greatest and least value.
  return max(l) - min(l)
