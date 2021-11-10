# SUM OF TWO NUMBERS IN A LIST EQUAL TO A GIVEN NUMBER EDABIT SOLUTION:

def check_sum(lst, n):
    
    # creating a for-loop to iterate through the list.
    for i in lst:
        
        # creating another for-loop to iterate through the list for a second element search.
        for j in lst:
             
            # creating a nested if-statement to check for the condition being met.
            if i + j == n:
                
                # returning 'True' if two elements are found that add up to 'n'.
                return True
     
    # returning 'False' if the two elements are not found.
    return False
