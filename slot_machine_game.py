import random
import time

def spin_slot():
    symbols = ['🍌','🍒','🔔','⭐','🍀']
    return [random.choice(symbols) for _ in range(3)]
def spin_animation():
    print("Spinning", end=" ")
    for _ in range(3):
        print('.', end=" ")
        time.sleep(0.5)
    print()
        
def print_spin(slot):
    print(" | ".join(slot))

def payout(slot, bet):
    if slot[0] == slot[1] == slot[2]:
        if slot[0] == '🍌':
            return bet * 3
        elif slot[0] == '🍒':
            return bet * 5
        elif slot[0] == '🔔':
            return bet * 6
        elif slot[0] == '⭐':
            return bet * 10
        elif slot[0] == '🍀':
            return bet * 50
    return 0  # lose

def main():
    print("======================")
    print("Welcome to Slot Game!")
    print("======================")

    balance = 100
    playing = True
    while playing:
        print(f"\nYou have ${balance} to play!")

        if balance <= 0:
            print("You have no balance!")
            print("Game Over!")
            break

        user_input = input("Enter bet amount (q to quit): ")

        if user_input.lower() == 'q':
            print("Thanks for playing!")
            break
        elif not user_input.isdigit():
            print("Invalid Input! ")
            continue

        bet = int(user_input)

        if bet > balance:
            print("Insufficient funds!")
            continue
        elif bet <= 0:
            print("Invalid bet amount!")
            continue

        balance -= bet

        slot = spin_slot()
        spin_animation()
        print_spin(slot)

        winnings = payout(slot, bet)
        balance += winnings

        if winnings > 0:
            print(f"You won ${winnings}!")
        else:
            print("You lost!")

if __name__ == '__main__':
    main()