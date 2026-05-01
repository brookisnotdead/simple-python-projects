import random
from word_list import words

# Drawings for each number of wrong guesses.
hangman = {0:("   ",
              "   ",
              "   "),
           1:(" o ",
              "   ",
              "   "),
           2:(" o ",
              " | ",
              "   "),
           3:(" o ",
              "/| ",
              "   "),
           4:(" o ",
              "/|\\",
              "   "),
           5:(" o ",
              "/|\\",
              "/  "),
           6:(" o ",
               "/|\\",
               "/ \\"),}


# Prints the hangman drawing based on the number of wrong guesses.
def display_hangman(wrong_guess):
    print("_____________________")
    for line in hangman[wrong_guess]:
        print(line)
    print("_____________________")


# Shows the current hint, such as "_ p p _ e".
def display_hint(hint):
    print(" ".join(hint))


# Shows the correct answer.
def display__answer(answer):
    print(" ".join(answer))


# Runs the Hangman game.
def main():
    print("Welcome To Hangman Game!")

    # Pick a random word and create one "_" for each letter.
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guess = 0

    # A set remembers letters that were already guessed.
    guessed_letter = set()
    is_playing = True
    while is_playing:
        display_hangman(wrong_guess)
        display_hint(hint)
        print()
        guess = input("Enter a guess: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!")
            continue

        # Prevent the same letter from being guessed twice.
        if guess in guessed_letter:
            print(f"{guess} is already guessed")
            continue

        guessed_letter.add(guess)

        # If the guessed letter is in the answer, reveal every matching position.
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        # If the guessed letter is wrong, add one wrong guess.
        if guess not in answer:
            wrong_guess += 1
            if wrong_guess == 6:
                display_hangman(wrong_guess)
                print("Game Over! Loser!")
                print(f"The correct word is {answer}")
                is_playing = False

        # The player wins when there are no "_" characters left.
        if "_" not in hint:
            print(f"You guessed the word {answer}!")
            print("CONGRATULATION!!!")
            is_playing = False
                            
            
        
        
    

# Starts the program only when this file is run directly.
if __name__ == "__main__":
    main()
