# SUM OF UNIQUE ELEMENTS LEETCODE SOLUTION:

class Solution(object):

    def sumOfUnique(self, nums):

        # creating a list to append the unique elements into.
        l = []

        # creating a for-loop to iterate for the elements in the array.
        for i in nums:

            # creating a nested if-statement to check for the element being present only once throughout the array.
            if nums.count(i) == 1:

                # code to append the element into the created list if the element is present only once.
                l.append(i)

        # returning the sum of the list with the unique elements.
        return sum(l)