# DETERMINE COLOR OF A CHESSBOARD SQUARE LEETCODE SOLUTION:

class Solution(object):

    def squareIsWhite(self, coordinates):
        
        # creating a dictionary with the correct amount of letters associated with their respective numbers.
        my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

        # creating variables and tying them to the two parts present in coordinates.
        letter, num = coordinates

        # creating an if-statement to check if the sum of the letter and number is even.
        if (my_dictionary[letter] + int(num)) % 2 == 0:

            # returning 'False' if the sum of the letter and number is even.
            return False

        # returning 'True' if the sum is odd and not even.
        return True