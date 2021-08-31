# SUM OF EVERY N'TH NUMBER EDABIT SOLUTION:

def sum_every_nth(numbers, n):
  
  # creating a variable to track the sum of every n'th number.
  summ = 0
  
  # creating a for-loop using enumerate to access the index and value of every element, while starting at 1.
  for idx, num in enumerate(numbers, 1):
    
    # creating a nested if-statement to check if the index is apart of every n'th number.
    if idx % n == 0:
      
      # code to add the value of the element at the n'th index if the condition is met.
      summ += num
  
  # returning the value for the sum of every n'th number.
  return summ
