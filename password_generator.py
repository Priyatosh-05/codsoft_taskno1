import random
import string
import os

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + symbols

    # Generate a password with at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to prevent predictable order
    random.shuffle(password)

    # Join the list to form the final password string
    return ''.join(password)

def main():
    try:
        os.system('cls')
        print("********************************************************************")
        length = int(input("Enter the desired password length (minimum 4): "))
        print("********************************************************************")
        if length < 4:
            print("Password length should be at least 4 for a strong password.")
            return
        
        while True:
            # Generate and display password
            password = generate_password(length)
            print("\n===============================")
            print("Generated Password:", password)
            print("===============================\n\n")
            
            # Ask if user wants to regenerate
            regenerate = input("Do you want to generate another password? (y/n): ").strip().lower()
            if regenerate != 'y':
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Final Password:", password)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                break

    except ValueError:
        print("Please enter a valid number.")

# Run the main function
main()
