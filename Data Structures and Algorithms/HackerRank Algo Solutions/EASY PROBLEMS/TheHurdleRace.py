# THE HURDLE RACE HACKER-RANK SOLUTION:

# creating a function to calculate the doses of potion during the race.
def hurdleRace(k, height):

    # creating an if-statement to determine how many potions are required. 
    if k > max(height):

        return '0'

    else:

        return max(height) - k

# receiving input.
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
height = list(map(int, input().rstrip().split()))

# printing the final output, which indicates the number of potions required.
result = hurdleRace(k, height)
print(result)