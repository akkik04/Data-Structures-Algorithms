# BINARY SEARCH IMPLEMENTED IN PYTHON RECURSIVELY:
# AKSHITH K

def binary_search(arr, target, mindex, maxdex):

    # checking the base case of the minimum index being greater than the maximum index.
    if mindex > maxdex:

        # returning 'None' to indicate that the search was exhausted and the desired element was not found.
        return None
    
    # creating a variable to store the midpoint in the array.
    mid = (mindex + maxdex) // 2

    # if the target is met at the midpoint.
    if arr[mid] == target:

        # returning the midpoint, as it is the index at which the element is present.
        return mid
    
    # if the midpoint is greater than the target.
    elif arr[mid] > target:

        # calling the recursive function, while increasing the minimum index by the value of the (midpoint + 1).
        return binary_search(arr, target, mid + 1, maxdex)
    
    # if the midpoint is less than the target.
    else:

        # calling the recursive function, while decreasing the maximum index by the value of the (midpoint - 1).
        return binary_search(arr, target, mindex, mid - 1)

# DRIVER CODE FOR TESTING THE ALGORITHM.
if __name__ == "__main__":

    arr = [2, 5, 99, 34, 21, 87, 98, 100, 2334, 211, 90, 21]
    target = 99

    print("The desired element is present at:", binary_search(arr, target, 0, len(arr) - 1))