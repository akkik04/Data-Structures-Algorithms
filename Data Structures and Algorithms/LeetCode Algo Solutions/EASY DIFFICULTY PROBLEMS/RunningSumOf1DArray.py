# RUNNING SUM OF 1D ARRAY LEETCODE SOLUTION:

class Solution(object):

    def runningSum(self, nums):

        # creating a variable to track the running sum.
        running_sum = 0

        # creating a list to append the running sum after each iteration.
        l = []

        # creating a for-loop to iterate for the elements in the array.
        for i in nums:

            # code to add each element into the running sum after each iteration.
            running_sum += i

            # code to append the sum after each iteration.
            l.append(running_sum)

        # returning the list with the running sum after each iteration.
        return l