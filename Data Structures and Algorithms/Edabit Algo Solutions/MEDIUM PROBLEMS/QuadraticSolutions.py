# HOW MANY SOLUTIONS DOES THIS QUADRARIC HAVE EDABIT SOLUTION:

# creating a function to solve the problem.
def solution(a, b, c):

    # creating a variable to track the discriminant.
    discriminant = b ** 2 - (4 * a * c)

    # returning the appropriate value according to the condition met.
    return 2 if discriminant > 0 else 1 if discriminant == 0 else 0