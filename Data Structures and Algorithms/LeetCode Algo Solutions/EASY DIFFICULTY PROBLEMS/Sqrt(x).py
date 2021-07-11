# SQRT(X) LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def mySqrt(self, x):

        # declaring a variable to track the output.
        i = 0

        # creating a while-loop to run while the output variable squared is less than or equal to the desired value.
        while i * i <= x:
            
            # incrementing the output variable's value.
            i += 1

        # returning the value of the output variable with modifications.
        return i - 1