# RETURN DUPLICATE NUMBERS EDABIT SOLUTION:

# creating a function to solve the problem.
def duplicate_nums(nums):
  
  # creating two lists.
  l1 = []
  l2 = []
  
  # creating a for-loop to iterate for the numbers.
  for i in nums:
    
    # creating a nested if-statement to append the elements into the first list.
    if i not in l1:
      
      # code to append the element into the first list if the condition is met.
      l1.append(i)
    
    # creating an else statement for handling the element being present in the first list already.
    else:
       
      # code to append the element that is already present in the first list, into the second list, as a duplicate.
      l2.append(i)
  
  # returning the list with the duplicates (l2) or 'None'.
  return l2 or None
