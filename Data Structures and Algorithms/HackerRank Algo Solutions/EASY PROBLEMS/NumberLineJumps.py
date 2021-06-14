# NUMBER LINE JUMPS HACKER-RANK SOLUTION:

# creating a function to calculate the meeting of the two kangaroos.
def kangaroo(x1, v1, x2, v2):

    # creating an if-statement to determine if the kangaroos will meet.
    if x1 < x2 and v1 < v2:
        return 'NO'
    else:
        if v1 != v2 and (x2 -x1) % (v1-v2) == 0:
            return 'YES'
        else:
            return 'NO'

# receiving input.  
first_multiple_input = input().rstrip().split()
x1 = int(first_multiple_input[0])
v1 = int(first_multiple_input[1])
x2 = int(first_multiple_input[2])
v2 = int(first_multiple_input[3])

# printing the final output, which indicates if the kangaroos meet. 
result = kangaroo(x1, v1, x2, v2)
print(result)