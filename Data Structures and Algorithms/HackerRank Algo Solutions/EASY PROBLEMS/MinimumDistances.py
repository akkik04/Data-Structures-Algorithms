# MINIMUM DISTANCES HACKERRANK SOLUTION:

# creating a function to find the minimum distance between equal elements.
def minimumDistances(n, a):

    # creating a list.
    listt = []

    # creating a for-loop to iterate for the list.
    for i in range(n - 1):

        # creating a nested for-loop to iterate based on the first-loop to find two equal elements.
        for j in range(i + 1, n):

            # creating a nested if-statement to check if the condition of similarity is met.
            if a[i] == a[j]:

                # code to calculate the index difference between the two elements.
                diff = j - i

                # code to append the difference into the list.
                listt.append(diff)

    # creating an if-statement to return the minimum distance between the various equal elements.
    if listt:

        # code to return the minimum distance if the condition is met.
        return min(listt)

    # returning '-1' if there are no equal elements in the given array.
    else:

        return -1

# receiving input.
n = int(input().strip())
a = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the minimum distance between various equal elements in the given array.
result = minimumDistances(n, a)
print(result)