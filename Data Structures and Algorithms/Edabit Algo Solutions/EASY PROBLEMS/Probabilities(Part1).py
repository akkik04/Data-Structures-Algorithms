# PROBABILITIES (PART 1) EDABIT SOLUTION:

def probability(lst, n):
  
  # creating a variable to store the length of the list.
  list_length = len(lst)
  
  # creating a variable to track the count of numbers that are greater than 'n'.
  count = 0
  
  # creating a for-loop to iterate for the elements in the list.
  for i in lst:
    
    # creating a nested if-statement to check for the condition of an element being greater than 'n'.
    if i >= n:
      
      # code to increment the count if the condition is met.
      count += 1
  
  # returning the probability of choosing a number greater than or equal to "n", while rounding to one decimal place.
  return round(((count / list_length) * 100), 1)
      
