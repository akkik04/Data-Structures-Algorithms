# SIGN OF THE PRODUCT OF AN ARRAY LEETCODE SOLUTION:

class Solution(object):

    def arraySign(self, nums):

        # creating a variable to track the product.
        product = 1

        # creating a for-loop to iterate for the given array.
        for i in nums:

            # creating a nested if-statement to check if '0' is present in the array.
            if 0 in nums:

                # returning '0' if the number 0 is present in the array because anything multiplied by 0 is 0.
                return 0

            else:

                # if no zero is detected then we continue calculating the product.
                product *= i

        # returning 1 if the sign of the product is positive, else -1 to indicate a negative sign of the product.
        return 1 if product > 1 else -1