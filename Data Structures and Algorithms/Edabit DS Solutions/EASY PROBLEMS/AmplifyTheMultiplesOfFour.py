# AMPLIFY THE MULTIPLES OF FOUR EDABIT SOLUTION:

def amplify(num):
  
  # creating a list to append the elements into for the amplification process.
  l = []
  
  # creating a for-loop to iterate for the elements until the given number.
  for i in range(1, num + 1):
    
    # creating a nested if-statement to check if the element is a multiple of four.
    if i % 4 == 0:
      
      # code to append the element, while amplifying it by 10.
      l.append(i * 10)
    
    else:
      
      # if the element is not a multiple of four, we simply append the element without any changes.
      l.append(i)
  
  # returning the list with the modified numbers.
  return l
