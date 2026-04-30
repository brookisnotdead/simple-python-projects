
import random
import string

chars = " " + string.punctuation + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

def encrypting(user_input):
    encrypted = ""
    for _ in user_input:
        index = key.index(_)
        encrypted += chars[index]
    print(f"Encrypted: {encrypted}")

def decrypting(user_input):
    decrypted = ""
    for _ in user_input:
        index = chars.index(_)
        decrypted += key[index]
    print(f"Decrypted: {decrypted}")


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
                
if __name__ == '__main__':
    main()