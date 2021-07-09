# ADD BINARY LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def addBinary(self, a, b):

        # using the 'bin' function to convert each integer into its binary format.
        sum = bin(int(a, 2) + int(b, 2))

        # returning the value of the sum, while truncating the '0b' prefix.
        return sum[2:]