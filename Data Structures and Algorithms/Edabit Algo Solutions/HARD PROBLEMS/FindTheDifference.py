# FIND THE DIFFERENCE EDABIT SOLUTION:

def find_the_difference(s, t):
  
  # creating a for-loop to iterate for the letters in string t, without duplications.
  for i in set(t):
    
    # creating a nested if-statement to check if the count of the element is not the same in string t and string s.
    if t.count(i) != s.count(i):
      
      # returning the element that satisfies the requirements.
      return i
