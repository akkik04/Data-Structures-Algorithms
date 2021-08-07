# WHERE IS BOB !?! EDABIT SOLUTION:

def find_bob(names):
  
  # creating a for-loop to iterate through the list of names.
  for i in range(len(nums)):
    
    # creating a nested if-statement to check for the name "Bob".
    if nums[i] == "Bob":
      
      # returning the index of the name if it is found in the list.
      return i
  
  # returning "-1" if the name "Bob" is not present within the list.
  return -1
