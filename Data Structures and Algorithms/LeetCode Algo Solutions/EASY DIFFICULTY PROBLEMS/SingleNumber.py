# SINGLE NUMBER LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def singleNumber(self, nums):
        
        # creating a variable and initializing it to '0'.
        x = 0
        
        # creating a for-loop to iterate for the nums.
        for i in nums:
            
            # utilizing the 'XOR' method as any number 'XOR' itself will get result 0, and a number XOR 0 will get itself. 
            x = i ^ x
        
        # returning the final single number after I 'XOR' numbers with each other.
        return x
