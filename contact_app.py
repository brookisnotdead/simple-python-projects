# Stores contact names and phone numbers.
contact ={}


# Adds a new contact to the dictionary.
def add_contact():
    name = input("Enter the name: ")
    number = int(input(f"Enter {name} number: "))
    contact.update({name : number})
    print("Contact has been added!")
    print()


# Removes a contact if the name exists.
def remove_contact():
    name = input("Enter the name: ")
    if name in contact.keys():
        contact.pop(name)
        print()
        print(f"{name} has been removed")
        print()


# Prints all saved contacts.
def list_contact():
    print("\nContact List!")
    for key, value in contact.items():
        print(f"\nName: {key}")
        print(f"Number: {value}")
        print("------------------------")
        print()


# Shows the menu and runs the contact app.
def main():
    using = True
    while using:
        print("1. Add contact")
        print("2. Remove contact")
        print("3. List contact")
        print("0. Exit.")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                add_contact()
            case 2:
                remove_contact()
            case 3:
                list_contact()
            case 0:
                break
            case _:
                print("Invalid input! ")
                continue


# Starts the program only when this file is run directly.
if __name__ == '__main__':
    main()
