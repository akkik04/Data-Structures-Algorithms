# ODDISH VS. EVENISH EDABIT SOLUTION:

def oddish_or_evenish(num):
  
  # creating a variable to track the sum of the digits of the number.
  sum = 0
  
  # creating a for-loop to iterate for the string version of the number.
  for i in str(num):
    
    # code to add each digit to the sum value of the digits. 
    sum += int(i)
  
  # creating an if-statement to check if the sum of the digits is even.
  if sum % 2 == 0:
    
    # returning 'Evenish' if the sum of the digits is even. 
    return "Evenish"
  
  # returning 'Oddish' if the sum of the digits is odd.
  return "Oddish"
