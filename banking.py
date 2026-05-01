# Shows the current balance.
def show_balance(balance):
    print(f"Balance: {balance}")


# Adds money to the balance if the amount is valid.
def deposit(amount, balance):
    if amount <= 0:
        print(f"Invalid deposit amount: {amount}")
        return balance
    else:
        balance += amount
        print(f"Deposit amount: {amount}")
        print(f"Balance: {balance}")
        return balance


# Subtracts money from the balance if there is enough money.
def withdraw(amount,balance):
    if balance <= amount:
        print(f"Insuffucient Balance: {balance}")
        return balance
    else:
        balance -= amount
        print(f"Withdraw amount: {amount}")
        print(f"Balance: {balance}")
        return balance


# Displays the menu and returns the user's choice.
def prompt():
    print(f"Simple bank sysytem!")
    print(f"1. Show balance")
    print(f"2. Deposit")
    print(f"3. Withdraw")
    choice = int(input(f"Enter your choice(0 to quit): "))
    return choice



# Runs the banking program.
def main():
    balance = 0
    running = True
    while running:
        choice = prompt()
        print()
        match choice:
            case 1:
                show_balance(balance)
                print()
            case 2:
                amount = float(input(f"Enter the amount: "))
                balance = deposit(amount, balance)
                print()
            case 3:
                amount = float(input(F"Enter the amount: "))
                balance = withdraw(amount,balance)
                print()
            case 0:
                print("Thank you!")
                print
                running = False
            case _:
                print(f"Invalid Action!")
                print()


# Starts the program only when this file is run directly.
if __name__ == '__main__':
    main()
