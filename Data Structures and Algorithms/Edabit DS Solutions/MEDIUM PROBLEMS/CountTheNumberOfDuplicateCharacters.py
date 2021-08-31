# COUNT THE NUMBER OF DUPLICATE CHARACTERS EDABIT SOLUTION:

def duplicates(txt):
  
  # creating a list to append the non-duplicate letters.
  l = []
  
  # creating a variable to track the count of duplicates.
  count = 0
  
  # creating a for-loop to iterate for the characters in the string.
  for i in txt:
    
    # creating a nested if-statement to append the non-duplicate characters.
    if i not in l:
      
      # code to append the non-duplicate characters.
      l.append(i)
    
    else:
      
      # code to increment the count of the duplicate characters if it is already present within the list.
      count += 1
  
  # returning the count of the duplicate characters.
  return count
