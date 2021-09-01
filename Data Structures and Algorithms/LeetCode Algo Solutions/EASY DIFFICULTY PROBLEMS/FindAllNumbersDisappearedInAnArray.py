# FIND ALL NUMBERS DISAPPEARED IN AN ARRAY LEETCODE SOLUTION:

class Solution(object):

    def findDisappearedNumbers(self, nums):

        # creating a variable to hold the list of the numbers, without duplicates.
        set_nums = set(nums)

        # creating a list to append the disappeared elements into.
        l = []

        # creating a for-loop to iterate for the length of the given array
        for i in range(1, len(nums) + 1):
            
            # creating a nested if-statement to check for the element not being present within the array.
            if i not in set_nums:

                # code to append the element that is not present within the array.
                l.append(i)
        
        # returning the list with the elements that were disappeared in the array.
        return l