# ANGRY PROFESSOR HACKERRANK SOLUTION:

# creating a function to find out if the class is cancelled.
def angryProfessor(k, a):

    # creating a variable to store the value of students that arrived on time.
    num_students = 0

    # creating a for-loop to iterate for the length of the array.
    for i in range(len(a)):

        # nested if-statement to determine the number of students that arrived on time.
        if a[i] <= 0:
            num_students += 1
    
    # creating an if-statement to determine if the number of students on time is less than the threshold.
    if num_students < k:

        # returning 'Yes' if the class is cancelled.
        return 'Yes'
    else:

        # returning 'No' if the class is running.
        return 'No'

# receiving input.
t = int(input().strip())
for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

# printing the final output, which indicatesthe status of the class.
result = angryProfessor(k, a)
print(result)