# FIND THE MEDIAN HACKERRANK SOLUTION:

# creating a function to find the median of the array.
def findMedian(arr):

    # code to sort the array.
    sorted_array = sorted(arr)

    # returning the median of the sorted array.
    return sorted_array[len(arr) // 2]

# receiving input.
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

# code to print the final output, which indicates the median of the array.
result = findMedian(arr)
print(result)