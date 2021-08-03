# FIND THE DISCOUNT EDABIT SOLUTION:

# creating a function to solve the problem.
def dis(price, discount):
   
  # code to find the amount saved from the discount.
  a = (price * discount) / 100
	
  # returning the final price after the discount, while rounding to two decimal places.
	return round(price - a, 2)
