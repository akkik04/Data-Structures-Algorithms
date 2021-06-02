# CATS AND A MOUSE HACKER-RANK SOLUTION:

# creating a function.
def catAndMouse(x, y, z):
    
    # findinf the absolute value of the distance from each cat to the mouse.
    CatA = abs(x-z)
    CatB = abs(y-z)

    # if-statement to determine which cat is closer.
    if CatA < CatB:
        return "Cat A"
    
    elif CatB < CatA:
        return "Cat B"
    
    else:
        return "Mouse C"

# input.
q = int(input())

for q_itr in range(q):

    xyz = input().split()

    x = int(xyz[0])

    y = int(xyz[1])

    z = int(xyz[2])

    # printing the output which indicates the cat that is closer to the mouse.
    print(catAndMouse(x, y, z))