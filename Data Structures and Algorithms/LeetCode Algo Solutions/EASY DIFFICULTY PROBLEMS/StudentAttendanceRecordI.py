# STUDENT ATTENDANCE RECORD I LEETCODE SOLUTION:

# creating a class.
class Solution:

    # creating a function to solve the problem.
    def checkRecord(self, s):

        # creating an if-statement to check if there was more than one absence.
        if s.count("A") > 1:

            # returning 'False' if the condition is met.
            return False

        # creating a for-loop to iterate for the given string.
        for i in range(len(s) - 2):

            # creating a nested if-statement to check if there were three consecutive lates.
            if s[i] == s[i + 1] == s[i + 2] == "L":

                # returning 'False' if the condition is met.
                return False

        # returning 'True' if nothing is stopping the perfect attendance.
        return True