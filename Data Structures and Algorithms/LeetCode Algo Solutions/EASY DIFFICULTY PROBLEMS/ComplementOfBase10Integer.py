# COMPLEMENT OF BASE 10 INTEGER LEETCODE SOLUTION:

class Solution(object):

    def bitwiseComplement(self, n):

        # creating an empty string to add the complement's bits into.
        x = " "

        # creating a for-loop to iterate for the binary version of 'n'.
        for i in bin(n)[2:]:

            # creating a nested if-statement to swap the 1's and 0's.
            if i is "0":

                # code to add "1" into the string if "0" is detected.
                x += "1"

            else:

                # code to add "0" into the string if "1" is detected.
                x += "0"

        # returning the integer version of the string with base 2.
        return int(x, 2)