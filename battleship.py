import random

# New empty list to simulate board game
board = []

# Add with append "0" to the board: 5 rows and 5 columns
for x in range(0,5):
  board.append(["O"] * 5)

# Function to print the board without "
def print_board(board):
  for row in board:
    print " ".join(row)

print "Let's play Battleship!"
print_board(board)

# Function to choose one position in the available rows ramdomly 
def random_row(board):
  return random.randint(0,len(board)-1)

# Function choose one position in the available columns ramdomly
def random_col(board):
  return random.randint(0,len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# User game begins. Only 4 turns!
for turn in range(4):
	guess_row = input("Guess Row:")
	guess_col = input("Guess Col:")
	
	#Winner turn :D
	if guess_row == ship_row and guess_col == ship_col:
	  print "Congratulations! You sunk my battleship!"
	  break
	#Looser turn :(
	else:
	  #Choosing right row and column
	  if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
	    print "Oops, that's not even in the ocean."
	  elif(board[guess_row][guess_col] == "X"):
	    print "You guessed that one already."
	  else:
	  	print "You missed my battleship!"
	  	board[guess_row][guess_col] = "X"
	  # Print (turn + 1) here!
	  print str(turn+1)
	  print_board(board)
	if turn==3:
		print "Game Over"