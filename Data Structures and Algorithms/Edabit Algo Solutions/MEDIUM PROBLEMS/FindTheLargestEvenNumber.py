# FIND THE LARGEST EVEN NUMBER EDABIT SOLUTION:

def largest_even(lst):
  
  # creating a variable to store the largest even number, initializing it to '-1' in the case that no even number is found.
  largest = -1
  
  # creating a for-loop to iterate for the elements in the list.
  for i in lst:
    
    # creating a nested if-statement to check if the number is even and larger than the previous largest even number.
    if i % 2 == 0 and i > largest:
      
      # making the largest number the number found in the list if the conditions are met.
      largest = i
  
  # returning the largest even number.
  return largest
