# EVEN NUMBER GENERATOR EDABIT SOLUTION:

def find_even_nums(num):
  
  # creating a list to append the even numbers into.
  l = []
  
  # creating a for-loop to iterate for the elements in the given number range.
  for i in range(1, num + 1):
    
    # creating a nested if-statement to check for the even elements in the list.
    if i % 2 == 0:
      
      # code to append the even elements into the list.
      l.append(i)
  
  # returning the list with the even numbers in the given range.
  return l
