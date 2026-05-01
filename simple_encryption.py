import random
import string

# All characters that can be encrypted.
chars = " " + string.punctuation + string.ascii_letters
chars = list(chars)

# Make a shuffled copy to act as the secret key.
key = chars.copy()
random.shuffle(key)


# Changes normal text into encrypted text.
def encrypting(user_input):
    encrypted = ""
    for _ in user_input:
        # Find the character in the key, then use the matching character from chars.
        index = key.index(_)
        encrypted += chars[index]
    print(f"Encrypted: {encrypted}")


# Changes encrypted text back into normal text.
def decrypting(user_input):
    decrypted = ""
    for _ in user_input:
        # Find the character in chars, then use the matching character from key.
        index = chars.index(_)
        decrypted += key[index]
    print(f"Decrypted: {decrypted}")


# Shows the menu and runs the encryption program.
def main():
    print("Simple Encryting System!")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    running = True
    while running:
        choice = int(input("What to do: "))
        match choice:
            case 1:
                user_input = input("What to Encrypt: ")
                encrypting(user_input) 
            case 2:
                user_input = input("What to Decrypt: ")
                decrypting(user_input)
            case 3:
                print("Exiting ....")
                running = False


# Starts the program only when this file is run directly.
if __name__ == '__main__':
    main()
