# TWO SUM LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def twoSum(self, nums, target):
        
        # creating for-loops to iterate through the array.
        for i in range(len(nums)):
            
            for j in range(i + 1, len(nums)):
                
                # creating a nested if-statement to determine what elements add up to the target.
                if nums[i] + nums[j] == target:

                    # returning the elements that satisfy the requirements.
                    return i, j