# ARE THE SUM OF DIGITS IN THE NUMBERS EQUAL EDABIT SOLUTION:

def is_equal(lst):
  
  # creating a list to append the sum of each digit
  l = []
  
  # creating a for-loop to iterate for each element in the list.
  for i in lst:
    
    # code to append the sum of each element in the list.
    l.append(sum(list(map(int, str(i)))))
  
  # returning if the sum's of all the digits are the same.
  # checking using the set() function, the set returns 1 if everything is same.
  return len(set(l)) == 1
