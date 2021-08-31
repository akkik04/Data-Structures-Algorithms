# LARGEST GAP EDABIT SOLUTION:

def largest_gap(lst):
  
  # creating a list to append the value for the gaps.
  gap = []
  
  # sorting the list.
  lst = sorted(lst)
  
  # creating a for-loop to iterate for the elements in the list.
  for i in range(len(lst)):
    
    # code to append the value for the gap between adjacent elements.
    gap.append(lst[i] - lst[i - 1])
  
  # returning the highest gap from the list.
  return max(gap)
