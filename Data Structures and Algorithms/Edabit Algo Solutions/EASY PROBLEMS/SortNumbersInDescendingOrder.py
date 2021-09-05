# SORT NUMBERS IN DESCENDING ORDER EDABIT SOLUTION;

def sort_descending(num):
  
  # turning the number into a list of its digits.
  num = list(map(int, str(num)))
  
  # creating a for-loop.
  for i in range(len(num)):
    
    # creating a nested for-loop 
    for j in range(len(num) - 1):
      
      # creating a nested if-statement to check for the element being smaller than the one in front of it.
      if num[j] < num[j + 1]:
        
        # performing the swapping of the elements to order it in descending fashion.
        num[j], num[j + 1] = num[j + 1], num[j]
  
  # returning the integer version of the list.
  return int("".join(map(str, num)))
