# REVERSE WORDS IN A STRING LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def reverseWords(self, s):

        # code to create a variable to store the split version of the given string.
        word_list = s.split()

        # code to reverse the split version of the string.
        word_list.reverse()

        # returning the string of the words in the reversed order.
        return " ".join(word_list)