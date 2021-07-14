# MAJORITY ELEMENT LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def majorityElement(self, nums):

        # code to sort the list of numbers.
        nums.sort()

        # returning the index that is the most present in the list.
        return nums[len(nums) // 2]