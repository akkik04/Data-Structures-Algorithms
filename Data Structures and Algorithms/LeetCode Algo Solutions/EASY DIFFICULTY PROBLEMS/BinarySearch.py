# BINARY SEARCH LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def binarySearch(self, nums, target):

        # creating a for-loop to iterate for the elements in the array.
        for i in range(len(nums)):

            # creating a nested if-statement to check if any element is our target.
            if nums[i] == target:
                
                # returning the index at which the element is found if the condition is met.
                return i

        # returning '-1' if the desired element is not present within the array.
        return -1