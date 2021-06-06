# DRAWING BOOK HACKER-RANK SOLUTION.

# creating a function to determine the minimum amount of flips requried.
def pageCount(n, p):

    # calculating the set target from the front (left-side) of the book.
    target_from_front = p // 2

    # if-statement to determine the target from the back (right-side) of the book.
    if n % 2 == 0:

        # if the total number of books is even, making it odd to avoid error.
        target_from_back = ((n+1) - p) // 2
    else:

        # if the total number of books is odd, simply calculating the flips.
        target_from_back = (n - p) // 2
    
    # returning the minimum value from each side of flipping the pages.
    return min(target_from_front, target_from_back)

# receiving input.
n = int(input().strip())
p = int(input().strip())

# printing the final output, which indicates the minimum amount of flips required.
result = pageCount(n, p)
print(result)