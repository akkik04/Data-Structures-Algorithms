# MIGRATORY BIRDS HACKER-RANK SOLUTION:

# function receiving parameter of the array.
def migratoryBird(arr):

    # initializing a list of zeroes.
    birds = [0] * len(arr)

    # creating a for-loop to iterate for the array.
    for i in range (len(arr)):

        # incrementing the count for each type of bird.
        birds[arr[i]] += 1
    
    # returning most common index.
    return birds.index(max(birds))


arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))

print(migratoryBird(arr))
