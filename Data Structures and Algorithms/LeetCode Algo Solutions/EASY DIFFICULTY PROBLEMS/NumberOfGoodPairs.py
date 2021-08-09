# NUMBER OF GOOD PAIRS LEETCODE SOLUTION:

class Solution(object):

    def numIdenticalPairs(self, nums):

        # creating a variable to keep track of the count for the good pairs.
        count = 0

        # creating a for-loop to iterate for the array of 'nums'.
        for i in range(len(nums)):

            # creating a nested for-loop to iterate based on the first-loop.
            for j in range(i + 1, len(nums)):

                # creating a nested if-statement to check if the conditions for a good pair are met.
                if nums[i] == nums[j]:

                    if i < j:

                        # code to increment the good pair count if all the conditions are satisfied.
                        count += 1

        # returning the value for the count variable.
        return count