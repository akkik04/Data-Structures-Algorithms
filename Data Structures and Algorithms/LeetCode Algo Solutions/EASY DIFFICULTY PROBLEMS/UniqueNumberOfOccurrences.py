# UNIQUE NUMBER OF OCCURRENCES LEETCODE SOLUTION:

# importing the collections module.
import collections

class Solution(object):

    def uniqueOccurrences(self, arr):

        # creating a variable to tie the occurence of each element in the array.
        x = collections.Counter(arr)

        # creating a list to append the occurrences into.
        l = []

        # creating a for-loop to iterate for the count of occurrences made by the 'Collections.counter()'.
        for i in x:

            # creating a nested if-statement to check if the count is already present within the list.
            if x[i] in l:

                # returning 'False' if the number of occurrence is already present, as it indicates a non-unique number.
                return False

            else:

                # code to append the count into the list if it is unique.
                l.append(x[i])

        # returning 'True' if no obstacle is met.
        return True