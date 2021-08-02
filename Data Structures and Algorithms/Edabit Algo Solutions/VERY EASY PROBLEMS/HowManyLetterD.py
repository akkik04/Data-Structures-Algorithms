# HOW MANY D'S ARE THERE? EDABIT SOLUTION:

# creating a function to solve the problem.
def count_d(sentence):
  
  # creating a variable to track the count of the letter 'D'.
  count = 0
  
  # creating a for-loop to iterate for the sentence.
  for i in sentence:
    
    # creating a nested if-statement to check if the letter 'D' is within the sentence.
    if i.count("D") or i.count("d"):
      
      # code to increment the count if the condition is met.
      count += 1
  
  # returning the count's value.
  return count
