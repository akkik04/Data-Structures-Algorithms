# NUMBER COMPLEMENT LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def findComplement(self, num):

        # creating a variable to store the number's complement.
        comp = " "

        # creating a for-loop to iterate through the binary version of the initial number.
        for i in bin(num)[2:]:

            # creating a nested if-statement to swap 0's with 1's and vice versa.
            if i is "0":

                # code to add the "1" in place of a "0" if the condition is met.
                comp += "1"

            else:

                # code to add the "0" in place of a "1" if the condition is met.
                comp += "0"

        # returning the complement in integer form with base 2.
        return int(comp, 2)