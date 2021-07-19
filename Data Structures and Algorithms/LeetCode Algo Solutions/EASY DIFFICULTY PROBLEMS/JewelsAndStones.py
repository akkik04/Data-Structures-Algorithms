# JEWELS AND STONES LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def numJewelsInStones(self, jewels, stones):

        # creating a variable to track the count.
        count = 0

        # creating a for-loop to iterate for the elements in the stones.
        for i in stones:
            
            # creating a nested if-statement to check if the elements in the stones are jewels.
            if i in jewels:
                
                # code to increment the count if the condition is met.
                count += 1

        # returning the value of the count.
        return count
