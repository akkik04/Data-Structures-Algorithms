# SINGLE NUMBER LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def singleNumber(self, nums):

        # creating a for-loop to iterate through the set of elements.
        for i in set(nums):

            # creating a nested if-statement to return the index of the element if it is found only once.
            if nums.count(i) == 1:

                # returning the element found only once if the condition is met.
                return i