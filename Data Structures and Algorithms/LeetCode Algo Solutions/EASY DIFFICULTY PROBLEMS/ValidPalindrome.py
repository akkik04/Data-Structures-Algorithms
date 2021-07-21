# VALID PALINDROME LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def isPalindrome(self, s):

        # creating a new string to add all the alphabets into.
        new = ''

        # creating a for-loop to iterate for the elements in the given string.
        for i in s:

            # creating a nested if-statement to check for alphabets or numbers.
            if i.isalnum():

                # code to add the element into the new string if the condition is met.
                new += i.lower()

        # returning if the string is a palindrome or not.
        return new == new[::-1]