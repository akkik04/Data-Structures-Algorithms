# APPLYING DISCOUNTS EDABIT SOLUTION:

def get_discounts(nums, d):
  
  # creating a list to append the new prices with the discount applied.
  l = []
  
  # creating a variable to store the discount.
  discount = int(d[:-1]) / 100
  
  # creating a for-loop to iterate for the prices in the given list.
  for i in nums:
    
    # appending the new price with the discount applied.
    l.append(i * discount)
  
  # returning the list with the modified prices.
  return l
