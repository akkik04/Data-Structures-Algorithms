# PLUS ONE LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def plusOne(self, digits):

        # returning the modified version of the array.
        return list(map(int, str(int(''.join(map(str,digits))) + 1)))