# COUNTING BITS LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def countBits(self, n):

        # returning the count of '1s' in the binary representation of 'i'.
        return[bin(i).count("1") for i in range(n + 1)]