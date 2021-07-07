# REMOVE DUPLICATES FROM SORTED ARRAY LEETCODE SOLUTION:

# creating a class.
class Solution(object):
    
    # creating a function to solve the problem.
    def removeDuplicates(self, nums):

        # creating a for-loop to iterate for the copy of the array.
        for i in nums[:]:

            # creating a nested if-statement to determine if any element occurs more than once. 
            if nums.count(i) > 1:

                # code to remove the element if it occurs more than once.
                nums.remove(i)

        # returning the modified array.
        return len(nums)