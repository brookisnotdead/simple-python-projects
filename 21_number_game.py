import random

# Game settings.
game_target = 21
min_move = 1
max_move = 3


# Prints the current count history.
def display_count(game_count):
    for count in game_count:
        print(count, end=" ")
    print()


# The game ends when the count reaches or passes 21.
def game_over(last_count):
    return last_count >= game_target




# Prints the winner based on who said the final number.
def display_winner(last_player):
    if last_player == "Player":
        print()
        print("You Lost Again Next Time!")
        print()
    elif last_player == "Bot":
        print()
        print("Player wins!")
        print()


# Resets the global game variables.
def reset_game():
    global last_count, game_count, last_player
    last_count = 0
    game_count = []
    last_player = ""


# Asks the player if they want to play another round.
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


# Chooses a random move for the bot.
def bot_move():
    return random.randint(min_move, max_move)


# Gets the player's move and makes sure it is 1, 2, or 3.
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


# Adds the player's or bot's move to the count.
def take_turn(player, move, last_count, game_count):
    print(f"{player} move: {move}")

    for _ in range(move):
        last_count += 1
        game_count.append(last_count)

        if game_over(last_count):
            break

    display_count(game_count)
    return last_count


# Lets the user choose whether to go first or second.
def chooce_player_take():
    while True:
        print("Enter F to play first")
        print("Enter S to play second")
        choice = input("Enter your choice: ")
        
        if choice.upper() == "F":
            return "Player"
        if choice.upper() == "S":
            return "Bot" 


# Runs one full round of the 21 number game.
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


# Runs the play-again loop.
def main():
    playing_again = True
    
    while playing_again:
        reset_game()
        game_start()
        playing_again = play_again()
        
    print("Thanks for playing!")


# Starts the program only when this file is run directly.
if __name__ == "__main__":
    main()
