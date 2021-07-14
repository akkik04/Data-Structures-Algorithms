# MISSING NUMBER LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def missingNumber(self, nums):

        # creating variables to store the values for the actual sum and the predicted sum.
        actual_sum = sum(nums)
        predicted_sum = 0

        # creating a for-loop to iterate for the elements in the array plus one to account for the missing number.
        for i in range(len(nums) + 1):

            # code to increment the predicted sum by each element for every iteration.
            predicted_sum += i
        
        # returning the difference between the two sums to find the missing number.
        return predicted_sum - actual_sum