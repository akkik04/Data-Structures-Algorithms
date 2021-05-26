# LIBRARY FINE HACKER-RANK SOLUTION:

# creating a function to determine the fine/penalty.
def libraryFine(d1, m1, y1, d2, m2, y2):

    # initializing the variable to store the value of the penalty.
    penalty = 0

    # if-statement to determine the total penalty.
    if y1 > y2:
        penalty += 10000

    elif y1 == y2 and m1 > m2:
        penalty += 500 * (m1-m2)
    
    elif y1 == y2 and m1 == m2 and d1 > d2:
        penalty += 15 * (d1 - d2)
    
    # returning the value of penalty.
    return penalty

# receiving inputs.
first_multiple_input = input().rstrip().split()
d1 = int(first_multiple_input[0])
m1 = int(first_multiple_input[1])
y1 = int(first_multiple_input[2])

second_multiple_input = input().rstrip().split()
d2 = int(second_multiple_input[0])
m2 = int(second_multiple_input[1])
y2 = int(second_multiple_input[2])

# printing the fine.
print(libraryFine(d1, m1, y1, d2, m2, y2))