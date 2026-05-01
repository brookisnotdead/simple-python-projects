

contact ={}
def add_contact():
    name = input("Enter the name: ")
    number = int(input(f"Enter {name} number: "))
    contact.update({name : number})
    print("Contact has been added!")
    print()

def remove_contact():
    name = input("Enter the name: ")
    if name in contact.keys():
        contact.pop(name)
        print()
        print(f"{name} has been removed")
        print()

def list_contact():
    print("\nContact List!")
    for key, value in contact.items():
        print(f"\nName: {key}")
        print(f"Number: {value}")
        print("------------------------")
        print()

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

if __name__ == '__main__':
    main()