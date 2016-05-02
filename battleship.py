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

#Makes guess of random row and column and assign them to ship_row and ship_col
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


