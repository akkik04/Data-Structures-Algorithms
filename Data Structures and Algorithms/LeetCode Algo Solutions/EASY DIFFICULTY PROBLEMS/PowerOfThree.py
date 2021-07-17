# POWER OF THREE LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def isPowerOfThree(self, n):

        # creating a variable to track the exponent.
        i = 0

        # creating a while-loop to iterate until the desired number.
        while 3 ** i <= n:
            
            # creating a nested if-statement to check if the desired number is met.
            if 3 ** i == n:
                
                # returning true if the condition is met.
                return True
            
            # code to increment the exponent by one after each iteration.
            i += 1

        # returning False if the condition is not met.
        return False 