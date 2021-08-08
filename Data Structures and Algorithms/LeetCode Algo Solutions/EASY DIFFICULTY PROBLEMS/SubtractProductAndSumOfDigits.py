# SUBTRACT THE PRODUCT AND SUM OF DIGITS OF AN INTEGER LEETCODE SOLUTION:

class Solution(object):

    def subtractProductAndSum(self, n):

        # creating a list of the digits for 'n'.
        x = map(int, str(n))

        # initializing variables to track the product and sum of the digits.
        digit_product = 1
        digit_sum = 0

        # creating a for-loop to iterate for the list of digits.
        for i in x:

            # code to multiply each element into the product.
            digit_product *= i

            # code to add each element into the sum.
            digit_sum += i

        # returning the difference between the product and sum.
        return digit_product - digit_sum 