# SET MISMATCH LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def findErrorNums(self, nums):

        # creating multiple variables to store various sums.
        actual_sum = sum(nums)
        set_sum = sum(set(nums))
        a_sum = len(nums) * (len(nums) + 1) / 2

        # returning the difference between appropriate sums.
        return [actual_sum - set_sum, a_sum - set_sum]