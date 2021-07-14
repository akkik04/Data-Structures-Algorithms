# FIND THE DUPLICATE NUMBER LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def findDuplicate(self, nums):

        # creating an iterable set.
        elements = set()

        # creating a for-loop to iterate for the elements in the list.
        for i in nums:

            # creating a nested if-statement to find the duplicated in the list.
            if i not in elements:

                # if the element is not initially present, we add it to the iterable set.
                elements.add(i)
            
            # creating an if-statement for returning the element if it is found more than once.
            else:

                # returning the element found more than once if the condition is met.
                return i
