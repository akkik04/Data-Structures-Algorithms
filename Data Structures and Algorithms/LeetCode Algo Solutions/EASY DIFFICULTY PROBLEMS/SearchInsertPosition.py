# SEARCH-INSERT-POSITION LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def searchInsert(self, nums, target):

        # creating an if-statement to check if the target is present within the array.
        if target in nums:
            
            return nums.index(target)
        

        # if the target is not within the array, we add the element to the array, sort the array, and return the index of the target.
        else:

            nums.append(target)
            nums.sort()
            
            return nums.index(target)