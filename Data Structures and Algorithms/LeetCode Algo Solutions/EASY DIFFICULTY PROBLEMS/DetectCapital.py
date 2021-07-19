# DETECT CAPITAL LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def detectCapitalUse(self, word):

        # returning if the word meets the conditions.
        return word == word.title() or word == word.lower() or word == word.upper()