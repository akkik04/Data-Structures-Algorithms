# FIND FIRST AND LAST POSITION OF ELEMENT IN SORTED ARRAY LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def searchRange(self, nums, target):

        # creating a list.
        l = []

        # creating an if-statement to check if the target is not within the given array.
        if target not in nums:

            # returning '[-1, -1]' if the condition is met.
            return -1, -1

        # creating a for-loop to iterate for the elements in the given array.
        for i in range(len(nums)):

            # creating a nested if-statement to check if the target is within the given array.
            if nums[i] == target:

                # code to append the index at which the target is present.
                l.append(i)

        # returning the first (minimum) and last (maximum) index of the element.
        return min(l), max(l)