# LENGTH OF LAST WORD LEETCODE SOLUTION:

# creating a class.
class Solution(object):
    
    # creating a function to solve the problem.
    def lengthOfLastWord(self, s):

        # creating a variable to split each word of a string into an item in a list.
        word_list = s.split()

        # creating an if-statement to determine the length of the last word.
        if len(word_list) == 0:

            # returning '0' if the last word does not exist.
            return '0'
        
        # returning the length of the last word if it exists.
        return len(word_list[-1])     