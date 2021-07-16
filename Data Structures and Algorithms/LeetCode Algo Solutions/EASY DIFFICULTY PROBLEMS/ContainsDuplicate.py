# CONTAINS DUPLICATE LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def containsDuplicate(self, nums):

        # returning if the set of numbers is equal to the actual numbers.
        # ** The 'set()' function takes away all duplicates, which means that if it is not equal to the len(nums), there are duplicates.
        return len(set(nums)) != len(nums)