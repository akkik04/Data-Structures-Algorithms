# REMOVE ELEMENT LEETCODE SOLUTION:

# creating a class.
class Solution(object):
    
    # creating a function to delete the desired number from a given array.
    def removeElement(self, nums, val):
        
        # creating a while-loop to iterate for the time that the value is present in the array.
        while val in nums:
            
            # code to remove the desired value.
            nums.remove(val)
        
        # returning the modified array.
        return(len(nums))