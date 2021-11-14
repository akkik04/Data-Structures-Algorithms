# CHESS BOARD SQUARES EDABIT SOLUTION:

def chess_board(pole):
  
  # creating a dictionary to relate the letter of each square to its respective letter.
  dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
  
  # creating variables to tie their values to the alphabet and numeric value of the given chess square.
  letter, num = pole
  
  # creating an if-statement to check for an even sum, indicating a 'black tile'.
  if (dictionary[letter] + int(num)) % 2 == 0:
    
    # returning that the given chess coordinate is a 'black tile' if the condition is met.
    return 'black'
  
  # returning 'white' if the tile is not 'black'.
  return 'white'
