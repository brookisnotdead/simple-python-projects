import random
SIZE = 4
TARGET = 2048



def add_two(board):
    empty = get_empty_slot(board)
    
    if not empty:
        return
    
    row, column = random.choice(empty)
    board[row][column] = 2 
        
def make_board():
    board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    add_two(board)
    return board
        
def display_board(board):
    
    for row in board:
        for number in row:
            if number == 0:
                print(f"{'.':>5}", end="")
            else:
                print(f"{number:>5}", end="")
        print()

def get_empty_slot(board):
    empty_slot = []
    
    for row in range(SIZE):
        for column in range(SIZE):
            if board[row][column] == 0:
                empty_slot.append((row, column))
    
    return empty_slot

def compress_row(row):
    numbers = []
    
    for number in row:
        if number != 0:
            numbers.append(number)
        
    while len(numbers) < SIZE:
        numbers.append(0)
        
    return numbers

def merge_row(row):
    row = compress_row(row)
    
    for i in range(SIZE - 1):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
            
    row = compress_row(row)
    return row

def move_left(board):
    new_board = []
    
    for row in board:
        new_row = merge_row(row)
        new_board.append(new_row)
        
    return new_board, new_board != board

def move_right(board):
    reversed_board = []
    
    for row in board:
        reversed_board.append(list(reversed(row)))
        
    moved_board, changed = move_left(reversed_board)
    
    new_board = []
    for row in moved_board:
        new_board.append(list(reversed(row)))
    
    return new_board, changed
        
        
def transpose(board):
    new_board = []
    
    for column in range(SIZE):
        new_row = []
        for row in range(SIZE):
            new_row.append(board[row][column])
        new_board.append(new_row)
    
    return new_board

def move_up(board):
    transpose_board = transpose(board)
    moved_board, changed = move_left(transpose_board)
    return transpose(moved_board), changed

def move_down(board):
    transpose_board = transpose(board)
    moved_board, changed = move_right(transpose_board)
    return transpose(moved_board), changed

def has_won(board):
    for row in board:
        for number in row:
            if number == TARGET:
                return True
            
    return False

def can_move(board):
    if get_empty_slot(board):
        return True
    
    for row in range(SIZE):
        for column in range(SIZE - 1):
            if board[row][column] == board[row][column + 1]:
                return True
            
    for row in range(SIZE - 1):
        for column in range(SIZE):
            if board[row][column] == board[row + 1][column]:
                return True
            
    
    return False
    
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



    
