import logic

def main():
    board = logic.make_board()
    
    print("WELCOME TO 2048 GAME!")
    print()
    print("Command list!")
    print("W to move up")
    print("A to move left")
    print("S to move down")
    print("D to move right")
    is_playing = True
    while is_playing:
        logic.display_board(board)
        
        if logic.has_won(board):
            print("You won the game")
            is_playing = logic.play_again()
            
        if not logic.can_move(board):
            print("You Lost! No more move available!")
            is_playing = logic.play_again()
        
        
        
        move = input("Enter Command: ")
        match move.lower():
            case "w":
                board, changed = logic.move_up(board)
            case "a":
                board, changed = logic.move_left(board)
            case "s":
                board, changed = logic.move_down(board)
            case "d":
                board, changed =logic.move_right(board)
            case _:
                print("Invalid Command!")
                continue
            
        if changed:
            logic.add_two(board)
        else:
            print("Nothing Move. Try other moves")
    

if __name__ =="__main__":
    main()