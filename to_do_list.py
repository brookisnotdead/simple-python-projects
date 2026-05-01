# Stores every to-do item the user adds.
to_do_list = []


# Lets the user add items to the to-do list.
def add_todo():
    print("Add things to do")
    adding = True
    while adding:
        todo = input("Enter Thing to do(q to quit): ")
        if todo.upper == 'Q':
            break
        else:
            to_do_list.append(todo)


# Prints all current to-do items.
def list_todo():
    # If the list is empty, there is nothing to show.
    if not to_do_list:
        print("There is nothing to do!")
        return False
    else:
        count = 1
        print("Things To Do!")
        for _ in to_do_list:
            print(f"{count}. {_}")
            count += 1


# Removes one item from the to-do list using its number.
def remove_todo():
    print("Remove Things From the list")
    running = True
    while running:
        list_todo()
        delete_list = int(input("What number of to do you want to remove(0 to quit): "))
        if delete_list == 0:
            print()
            break
        else:
            delete_list -= 1
            to_do_list.remove(to_do_list[delete_list])
    


# Shows the menu and runs the main program loop.
def main():
    running = True
    while running:
        print("Welcome to my simple to do list!")
        print("1. add To Do")
        print("2. Remove To Do")
        print("3. List To Do")
        print("0. Exit.")
        choice = int(input("Enter your  choice: "))
        match choice:
            case 1:
                add_todo()
            case 2:
                remove_todo()
            case 3:
                list_todo()
            case 0:
                print("Thank You For Using My To Do List!")
                break
            case _:
                print("Invalid input!")
                continue


# Starts the program only when this file is run directly.
if __name__ == '__main__':
    main()
    
