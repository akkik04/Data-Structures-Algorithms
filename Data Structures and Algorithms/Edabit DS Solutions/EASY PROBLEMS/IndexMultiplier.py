# INDEX MULTIPLIER EDABIT SOLUTION:

def index_multiplier(lst):
  
  # creating a variable to store the sum.
  summ = 0
  
  # creating a for-loop using 'enumerate' to access the index and the value.
  for idx, num in enumerate(nums):
    
    # code to add the product of the index and value to the sum variable.
    summ += (idx * num)
  
  # returning the value of the sum.
  return summ
  
