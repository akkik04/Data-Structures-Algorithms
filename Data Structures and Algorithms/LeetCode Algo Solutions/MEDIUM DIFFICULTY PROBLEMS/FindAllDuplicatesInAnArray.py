# FIND ALL DUPLICATES IN AN ARRAY:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def findDuplicates(self, nums):

        # creating a list to store the duplicate numbers.
        dup_array = []

        # code to sort the given list of numbers.
        nums.sort()

        # creating a for-loop to iterate for the elements in the given list.
        for i in range(1, len(nums)):
            
            # creating a nested if-statement to check if adjacent elements are the same.
            if nums[i] == nums[i - 1]:

                # code to append the element into the 'dup_array' if the condition is met.
                dup_array.append(nums[i])

        # returning the list that has the duplicate numbers.
        return dup_array