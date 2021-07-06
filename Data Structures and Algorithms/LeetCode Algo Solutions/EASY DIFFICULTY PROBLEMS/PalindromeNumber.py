# PALINDROME NUMBER LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def isPalindrome(self, x):
        
        # converting the given integer into a string.
        y = str(x)
        
        # created an if-statement to check if the original and reversed string is the same.
        if y == y[::-1]:

            # returning true if the number is a palindrome.
            return True

        else:

            # returning false if the number is not a palindrome.
            return False
        