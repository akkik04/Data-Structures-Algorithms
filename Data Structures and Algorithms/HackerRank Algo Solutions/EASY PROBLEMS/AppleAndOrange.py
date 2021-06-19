# APPLE AND ORANGE HACKERRANK SOLUTION:

# creating a function to calculate the number of apples and oranges.
def countApplesandOranges(s, t, a , b, apples, oranges):

    # declaring variables to store the value for the number of apples and oranges.
    number_of_apples = 0
    number_of_oranges = 0

    # creating a for-loop to iterate for the length of the apples array.
    for i in range(len(apples)):

        # creating a nested if-statement to increment the number of apples in the vicinity of the house if the conditions are met.
        if a + apples[i] >= s and a + apples[i] <= t:
            number_of_apples += 1
    
    # creating a for-loop to iterate for the length of the oranges array.
    for j in range(len(oranges)):

        # creating a nested if-statement to increment the number of oranges in the vicinity of the house if the conditions are met.
        if b + oranges[j] >= s and b + oranges[j] <= t:
            number_of_oranges += 1
    
    # printing the number of apples and oranges in the vicinity of the house.
    print(number_of_apples)
    print(number_of_oranges)
    

# receiving input.
first_multiple_input = input().rstrip().split()
s = int(first_multiple_input[0])
t = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()
a = int(second_multiple_input[0])
b = int(second_multiple_input[1])

third_multiple_input = input().rstrip().split()
m = int(third_multiple_input[0])
n = int(third_multiple_input[1])

apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))

countApplesandOranges(s, t, a, b, apples, oranges)