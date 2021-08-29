# IS JOHNNY MAKING PROGRESS EDABIT SOLUTION:

def progress_days(runs):
  
  # creating a variable to track the count for the number of days that progress is made.
  count = 0
  
  # creating a for-loop to iterate for the elements in the list.
  for i in range(1, len(runs)):
    
    # creating a nested if-statement to check if the current element is greater than the previous element.
    if runs[i] > runs[i - 1]:
      
      # code to increment the count if the condition is met.
      count += 1
  
  # returning the count of the days with progress.
  return count
