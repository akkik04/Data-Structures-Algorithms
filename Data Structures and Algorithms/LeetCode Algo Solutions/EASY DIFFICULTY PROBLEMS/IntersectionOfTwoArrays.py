# INTERSECTION OF TWO ARRAYS LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def intersection(self, nums1, nums2):

        # returning the intersection between the two arrays.
        return list(set(nums1).intersection(set(nums2)))