# VALID ANAGRAM LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def isAnagram(self, s, t):

        # returning if the sorted version of 't' is an anagram of the sorted version of 's'.
        return sorted(s) == sorted(t)