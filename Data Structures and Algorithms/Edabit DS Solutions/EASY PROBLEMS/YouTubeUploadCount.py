# YOUTUBE UPLOAD COUNT EDABIT SOLUTION:

def upload_count(dates, month):
  
  # creating a variable to track the count of uploads for a given month.
  count = 0
  
  # creating a for-loop to iterate for the dates in the list.
  for i in range(len(dates)):
    
    # creating a nested if-statement to check if the month is present within an element, this indicates that the upload relates to that month.
    if month in dates[i]:
      
      # code to increment the count variable if the condition is met.
      count += 1
      
  # returning the value of the count.
  return count
