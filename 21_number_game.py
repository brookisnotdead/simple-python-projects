import random
game_target = 21
min_move = 1
max_move = 3

def display_count(game_count):
    for count in game_count:
        print(count, end=" ")
    print()
    
def game_over(last_count):
    return last_count >= game_target




def display_winner(last_player):
    if last_player == "Player":
        print()
        print("You Lost Again Next Time!")
        print()
    elif last_player == "Bot":
        print()
        print("Player wins!")
        print()
        
def reset_game():
    global last_count, game_count, last_player
    last_count = 0
    game_count = []
    last_player = ""

def play_again():
    while True:
        choice = input("Do you want to play again? (Y/N): ")
        if choice.upper() == "Y":
            return True
        elif choice.upper() == "N":
            return False
        else:
            print("Invalid choice!")
            continue

def bot_move():
    return random.randint(min_move, max_move)

def player_move():
    while True:
        try:
            move = int(input("Enter how many moves you want to take (1-3): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if min_move <= move <= max_move:
            return move

        print("Invalid move. You can only move 1-3!")

def take_turn(player, move, last_count, game_count):
    print(f"{player} move: {move}")

    for _ in range(move):
        last_count += 1
        game_count.append(last_count)

        if game_over(last_count):
            break

    display_count(game_count)
    return last_count
       
    
def chooce_player_take():
    while True:
        print("Enter F to play first")
        print("Enter S to play second")
        choice = input("Enter your choice: ")
        
        if choice.upper() == "F":
            return "Player"
        if choice.upper() == "S":
            return "Bot" 
    

def game_start():
    last_count = 0
    game_count = []
    last_player = ""
    current_player = chooce_player_take()
    while not game_over(last_count):
        if current_player == "Player":
            move = player_move()
            last_count = take_turn("Player", move, last_count, game_count)
            last_player = "Player"
            current_player = "Bot"
        else:
            move = bot_move()
            last_count = take_turn("Bot", move, last_count, game_count)
            last_player = "Bot"
            current_player = "Player"

    print("The game is over")
    display_winner(last_player)
        

def main():
    playing_again = True
    
    while playing_again:
        reset_game()
        game_start()
        playing_again = play_again()
        
    print("Thanks for playing!")
        

if __name__ == "__main__":
    main()
