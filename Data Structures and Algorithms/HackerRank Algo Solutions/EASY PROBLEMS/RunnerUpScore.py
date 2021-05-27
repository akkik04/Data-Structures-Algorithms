# FIND THE RUNNER-UP SCORE HACKER-RANK SOLUTION:

# receiving input.
n = int(input())
arr =list(map(int, input().split()))

# sorting the array.
sorted_arr = arr.sort()

# printing the second greatest index.
print(arr[(arr.index(max(arr)))-1])