# BREAKING THE RECORDS HACKERRANK SOLUTION:

# creating a function to calculate amount of times the max and min records were broken.
def breakingRecords(scores):

    # creating variables and initially declaring the minimum and maximum values to the first value of the array.
    minimum = scores[0]
    maximum = scores[0]

    # creating variables to store the count for the max and min values being broken.
    max_broken_count = 0
    min_broken_count = 0
    
    # creating a for-loop to iterate for the length of the array.
    for i in range(len(scores)):

        # creating an if-statement to determine when to increment the count for the max and min values being broken.
        if scores[i] > maximum:
            
            # re-writing the new maximum if a higher value is found.
            maximum = scores[i]

            # incrementing the count for number of times the max score was broken.
            max_broken_count += 1
        
        elif scores[i] < minimum:
            
            # rewriting the new minimum if a lower value is found.
            minimum = scores[i]

            # incrementing the count for the number of times the min score was broken.
            min_broken_count += 1

    # code to return the max and min counts.
    return [max_broken_count, min_broken_count]

# receiving input.
n = int(input().strip())
scores = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the number of times the max and min score was broken.
result = breakingRecords(scores)
print(result)