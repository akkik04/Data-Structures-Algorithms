# FIND THE DIFFERENCE LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def findTheDifference(self, s, t):

        # code to update the strings by sorting and making them into lists.
        s = sorted(list(s))
        t = sorted(list(t))

        # creating a variable to track the indexes while looping.
        i = 0

        # creating a while-loop to iterate for the new list 't', while making sure that the elements in both lists are equal.
        while i < len(t) - 1 and s[i] == t[i]:

            # code to increment the index variable if the conditions are met after each iteration.
            i += 1
        
        # returning the different element that is found when the while-loop is broken.
        return t[i]

