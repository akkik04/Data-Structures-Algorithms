# ADD TO ARRAY FORM OF INTEGER LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def addToArrayForm(self, num, k):

        # creating a variable to hold the string version of the number.
        res = ''

        # creating a for-loop to iterate for the elements in the array.
        for i in num:
            
            # code to add the string element into the created variable.
            res += str(i)

        # code to add the desired value while performing the appropriate type-casting.
        res = str(int(res) + k)

        # code to split the string number into each seperate digit.
        res.split()

        # returning the array-form of the final integer.
        return res