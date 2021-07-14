# MULTIPLY STRINGS LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def multiply(self, num1, num2):

        # converting the given strings to integers.
        num1 = int(num1)
        num2 = int(num2)

        # code to find the product of the integers.
        product = num1 * num2
        
        # returning the product as a string.
        return str(product)