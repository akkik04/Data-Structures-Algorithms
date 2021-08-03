# FIZZ BUZZ LEETCODE SOLUTION:

# creating a class.
class Solution(object):

    # creating a function to solve the problem.
    def fizzBuzz(self, n):

        # creating a list.
        x = []

        # creating a for-loop to iterate for the numbers in range on 'n'.
        for i in range(1, n + 1):
            
            # creating several nested if-statements for handling the element differently depending on the condition.
            if i % 3 == 0 and i % 5 == 0:

                # code to append 'FizzBuzz' if the condition is met.
                x.append("FizzBuzz")

            elif i % 3 == 0:

                # code to append 'Fizz' if the condition is met.
                x.append("Fizz")

            elif i % 5 == 0:

                # code to append 'Buzz' if the condition is met.
                x.append("Buzz")
            
            else:

                # code to append the string version of the element itself if none of the conditions are met.
                x.append(str(i))

        # returning the list.
        return x