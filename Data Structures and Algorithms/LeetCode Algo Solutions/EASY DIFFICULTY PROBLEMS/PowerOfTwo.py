# POWER OF TWO LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def isPowerOfTwo(self, n):

        # creating a variable to track each number.
        i = 0

        # creating a while-loop to iterate till the given integer.
        while 2 ** i <= n:

            # creating a nested if-statement to check if the number variable is a power of two.
            if 2 ** i == n:

                # returning True if the condition is met.
                return True
            
            # code to increment the number we check each time by one.
            i += 1

        # returning False if the condition is not met.
        return False
