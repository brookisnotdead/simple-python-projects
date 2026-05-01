import random


# Creates the 4 random numbers that the player needs to guess.
def num_to_guess():
    to_guess = []
    for _ in range(4):
        num = random.randint(0, 9)
        to_guess.append(num)
    return to_guess


# Shows the hint, such as "_ 2 _ 5".
def display_hint(hint):
    print(" ".join(hint))


# Gets a valid 4-digit guess from the player.
def get_guess():
    while True:
        guess = input("Enter you guess: ")
        if len(guess) == 4 and guess.isdigit():
            return guess
        else:
            print("Invalid Guess! ")
            continue


# Asks the player if they want another round.
def play_again():
    while True:
        choice = input("Do you want to play again(y/n)?")
        if choice.upper() == "Y":
            print("Welcome to Mastermind Game!")
            return True
        if choice.upper() == "N":
            print("Thank you for playing!")
            print("Exiting...")
            return False
        else:
            print("Invalid Input!")
            continue


# Runs the Mastermind game.
def main():
    to_guess = num_to_guess()

    # Each "_" means that position has not been guessed correctly yet.
    hint = ["_"] * 4
    tries = 0
    print("WELCOME TO MASTERMIND GAME!")
    is_playing = True
    while is_playing:
        guess = get_guess()
        guess = [int(i) for i in str(guess)]

        # Track if this guess has at least one correct number in the correct position.
        got_correct_guess = False
        for i in range(len(to_guess)):
            if guess[i] == to_guess[i]:
                hint[i] = str(guess[i])
                got_correct_guess = True    
        
        if got_correct_guess:
            print("You got a correct number!")
        else:
            print("You got nothing correct!")
            tries += 1
        display_hint(hint)

        # If no "_" is left, all numbers have been guessed.
        if "_" not in hint:
            print("You Finish The Game!")
            print(f"It take's {tries} tries to guess {display_hint}")
            print("Congratulation!")
            is_playing = play_again()


# Starts the program only when this file is run directly.
if __name__ == "__main__":
    main()
