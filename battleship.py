from random import randint #Import randint from random to help in generating random numbers

#Creaate a empty list
board = []

#Append 5 lists (with "0") into board
for x in range(0, 5):
    board.append(["O"] * 5)

#Iterates through all lists joining the elements using a space
def print_board(board):
    for row in board:
        print " ".join(row)

#First instance off printing the board so far
print_board(board)

#Makes guess of ship_row number and ship_col number
#Prompt the input of the user to input numbers for the col and row
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))


#Print the randomised column and row number
#Check

print ship_row
print ship_col

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
else:
    print "You missed my battleship!"

#Append letter "X" to the user's guess numbers to positon and print it
board[guess_row][guess_col] = "X"

print board
