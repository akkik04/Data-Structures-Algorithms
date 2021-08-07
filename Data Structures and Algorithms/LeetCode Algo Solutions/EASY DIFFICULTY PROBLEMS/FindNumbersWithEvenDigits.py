# FIND NUMBERS WITH EVEN NUMBER OF DIGITS SOLUTION:

class Solution(object):

    def findNumbers(self, nums):

        # creating a variable to track the count.
        count = 0

        # creating a for-loop to iterate for the elements in the array.
        for i in nums:

            # creating a nested if-statement to check for the even number of digits of an element.
            if len(str(i)) % 2 == 0:

                # incrementing the count if the condition is met.
                count += 1

        # returning the value of the count.
        return count