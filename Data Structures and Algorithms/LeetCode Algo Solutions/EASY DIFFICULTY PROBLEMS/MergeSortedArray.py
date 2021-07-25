# MERGE SORTED ARRAY LEETCODE SOLUTION:

'''
We simply modify the array and do not return anything as expected from the problem's description.
'''

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def merge(self, nums1, m, nums2, n):

        # creating a for-loop to iterate from the unwanted numbers to the end of the first array.
        for i in range(m, len(nums1)):

            # code to delete all the unwanted numbers, which are '0'.
            nums1.pop()

        # creating a second for-loop to iterate for the elements in the second array.
        for j in nums2:

            # code to append the elements in the second array into the first array.
            nums1.append(j)

        # code to sort the elements in the first array.
        nums1.sort()