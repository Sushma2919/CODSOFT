import random
import string

def generate_password():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter desired password length: "))
        if length < 1:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Define character sets for complexity
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Display the password
    print(f"Generated Password: {password}")

# Run the function
generate_password()
