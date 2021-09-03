# LINEAR SEARCH IMPLEMENTED IN PYTHON RECURSIVELY
# AKSHITH K

def linear_search(arr, element, left, right):

    # checking if the right pointer is less than the left pointer.
    if right < left:

        # returning 'None' to indicate that the desired element is not present within the list after searching.
        return None
    
    # if the right-pointer holds the desired element.
    elif arr[right] == element:

        # returning the right-pointer's value as it is the index at which the element is at.
        return right
    
    # if the left-pointer holds the desired element.
    elif arr[left] == element:

        # returning the left-pointer's value as it is the index at which the element is at.
        return left
    
    # calling the recursive function.
    return linear_search(arr, element, left + 1, right - 1)

# DRIVER CODE FOR TESTING THE ALGORITHM.
if __name__ == "__main__":
    
    arr = [3, 12, 90, 45, 76, 99, 32, 22, 31, 7]
    element = 0
    print("The desired element is present at index:", linear_search(arr, element, 0, len(arr) - 1))