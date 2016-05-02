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
