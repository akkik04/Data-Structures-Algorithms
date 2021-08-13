# CHECK IF THE SENTENCE IS PANGRAM LEETCODE SOLUTION:

# 2 SOLUTIONS PROVIDED:

# 1st Solution.
class Solution(object):

    def checkIfPangram(self, sentence):

        '''
        METHOD 1: USING THE FOR-LOOP TO LOOP THROUGH THE ALPHABETS AND FINDING IF EACH IS PRESENT IN THE SENTENCE OR NOT.
        '''

        # creating a variable to store all the alphabets.
        alphabets = "abcdefghijklmnopqrstuvwxyz"

        # creating a for-loop to iterate for the alphabets.
        for i in alphabets:

            # creating a nested if-statement to check if any alphabet is not present in the given sentence.
            if i not in sentence:

                # returning False if the condition is met, indicating that the sentence is not a pangram due to the lack of letter(s).
                return False

        # returning True if the pangram is detected and no letters are missing from the sentence.
        return True

# 2nd Solution.
class Solution2(object):

    def checkIfPangram(self, sentence):

        '''
        METHOD 2: USING THE SET() FUNCTION TO CHECK IF THE LENGTH OF THE SENTENCE WOULD BE THE NUMBER OF ENGLISH ALPHABETS.
        '''

        # returning a boolean value for the length of the sentence equalling '26' after using the set() function.
        return len(set(sentence)) == 26