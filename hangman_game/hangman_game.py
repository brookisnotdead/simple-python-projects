import random
from word_list import words

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

def display_hangman(wrong_guess):
    print("_____________________")
    for line in hangman[wrong_guess]:
        print(line)
    print("_____________________")

def display_hint(hint):
    print(" ".join(hint))

def display__answer(answer):
    print(" ".join(answer))

def main():
    print("Welcome To Hangman Game!")
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guess = 0
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
        
        if guess in guessed_letter:
            print(f"{guess} is already guessed")
            continue
        
        guessed_letter.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                    
        if guess not in answer:
            wrong_guess += 1
            if wrong_guess == 6:
                display_hangman(wrong_guess)
                print("Game Over! Loser!")
                print(f"The correct word is {answer}")
                is_playing = False
        
        if "_" not in hint:
            print(f"You guessed the word {answer}!")
            print("CONGRATULATION!!!")
            is_playing = False
                            
            
        
        
    

if __name__ == "__main__":
    main()