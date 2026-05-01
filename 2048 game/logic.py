import random

# The board is 4 rows by 4 columns.
SIZE = 4

# The player wins when any tile reaches this number.
TARGET = 2048


# add number 2 in empty slot
def add_two(board):
    # Get all empty positions first so the new 2 can be placed randomly.
    empty = get_empty_slot(board)
    
    # If there are no empty slots, do not add anything.
    if not empty:
        return
    
    row, column = random.choice(empty)
    board[row][column] = 2 
    
# makes the 4 * 4 board
def make_board():
    board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    add_two(board)
    return board

# displays the latest board        
def display_board(board):
    # Print each row, then print each number inside that row.
    for row in board:
        for number in row:
            if number == 0:
                # Show empty spaces as dots so the board is easier to read.
                print(f"{'.':>5}", end="")
            else:
                print(f"{number:>5}", end="")
        print()

# finds empty slot in the board
def get_empty_slot(board):
    empty_slot = []
    
    # Check every row and column in the board.
    for row in range(SIZE):
        for column in range(SIZE):
            if board[row][column] == 0:
                # Save the position of every empty cell.
                empty_slot.append((row, column))
    
    return empty_slot


# Moves all non-zero numbers in one row to the left.
# Example: [2, 0, 4, 0] becomes [2, 4, 0, 0].
def compress_row(row):
    numbers = []
    
    for number in row:
        if number != 0:
            numbers.append(number)
        
    while len(numbers) < SIZE:
        numbers.append(0)
        
    return numbers

# Combines matching numbers beside each other in one row.
# Example: [2, 2, 4, 0] becomes [4, 4, 0, 0].
def merge_row(row):
    # Compress first so numbers slide left before merging.
    row = compress_row(row)
    
    for i in range(SIZE - 1):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    
    # Compress again to remove the zero left behind after merging.
    row = compress_row(row)
    return row

# Moves every row to the left and tells the main program if the board changed.
def move_left(board):
    new_board = []
    
    for row in board:
        new_row = merge_row(row)
        new_board.append(new_row)
        
    return new_board, new_board != board

# To move right, reverse each row, move left, then reverse each row back.
def move_right(board):
    reversed_board = []
    
    for row in board:
        reversed_board.append(list(reversed(row)))
        
    moved_board, changed = move_left(reversed_board)
    
    new_board = []
    for row in moved_board:
        new_board.append(list(reversed(row)))
    
    return new_board, changed
        
# Turns rows into columns.
# This helps reuse move_left and move_right for up and down movement.
def transpose(board):
    new_board = []
    
    for column in range(SIZE):
        new_row = []
        for row in range(SIZE):
            new_row.append(board[row][column])
        new_board.append(new_row)
    
    return new_board

# To move up, turn columns into rows, move left, then turn them back.
def move_up(board):
    transpose_board = transpose(board)
    moved_board, changed = move_left(transpose_board)
    return transpose(moved_board), changed

# To move down, turn columns into rows, move right, then turn them back.
def move_down(board):
    transpose_board = transpose(board)
    moved_board, changed = move_right(transpose_board)
    return transpose(moved_board), changed

# Checks if the player has reached the target tile.
def has_won(board):
    for row in board:
        for number in row:
            if number == TARGET:
                return True
            
    return False

# Checks if the player can still make a move.
def can_move(board):
    # If there is an empty slot, the game can continue.
    if get_empty_slot(board):
        return True
    
    # Check if any side-by-side numbers can merge horizontally.
    for row in range(SIZE):
        for column in range(SIZE - 1):
            if board[row][column] == board[row][column + 1]:
                return True
    
    # Check if any up-and-down numbers can merge vertically.
    for row in range(SIZE - 1):
        for column in range(SIZE):
            if board[row][column] == board[row + 1][column]:
                return True
    
    # If there are no empty slots and no possible merges, the game is over.
    return False

# Asks the player if they want to start another game.
def play_again():
    while True:
        choice = input("Do you want to pay again?(Y/N): ")
        if choice.lower() == 'y':
            print("Game Start!")
            return True
        
        elif choice.lower() == 'n':
            print("Thank you for playing!")
            print("Exiting . . .")
            return False
        else:
            print("Invalid!")
            continue



    
