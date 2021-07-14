# SORT COLORS LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def sortColors(self, nums):

        # creating a for-loop to iterate for the list of elements.
        for i in range(len(nums)):

            # creating a nested for-loop to iterate for the adjacent elements in the list.
            for j in range(i + 1, len(nums)):

                # creating a nested if-statement to check if the elements are not in the right place.
                if nums[i] > nums[j]:
                    
                    # code to switch the elements if the condition is met.
                    nums[i], nums[j] = nums[j], nums[i]

        # returning the sorted list of numbers.
        return nums