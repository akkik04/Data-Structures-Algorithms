# REMOVING ENEMIES EDABIT SOLUTION:

def remove_enemies(names, enemies):
  
  # creating a list to append the non-enemies.
  l = []
  
  # creating a for-loop to iterate for the names.
  for i in names:
    
    # creating a nested if-statement to check if the name is a non-enemy.
    if i not in enemies:
      
      # code to append the non-enemy into the list.
      l.append(i)
  
  # returning the list with the enemies removed.
  return l
