# FIND PIVOT INDEX LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def pivotIndex(self, nums):

        # creating a variable to store the leftsides sum.
        left_sum = 0

        # creating a variable to store the rightsides sum, intializing it to the sum of all the nums.
        right_sum = sum(nums)

        # creating a for-loop to iterate for the elements in the array.
        for i in range(len(nums)):

            # code to decrease the rightsides sum by the value of the index after each iteration.
            right_sum -= nums[i]

            # creating a nested if-statement to check if there is a point where both sides are equal.
            if left_sum == right_sum:

                # returning the index if the condition is met.
                return i
            
            # code to increase the leftsides sum by the value of the index after each iteration.
            left_sum += nums[i]

        # returning '-1' if there is not any index that satisfies the requirements.
        return -1