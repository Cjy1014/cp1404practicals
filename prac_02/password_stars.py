def main():
    MIN_LENGTH = 6

    password = get_password(MIN_LENGTH)
    print_asterisks(password)

def get_password(min_length):
    """Prompt user for a valid password, ensuring it meets the minimum length requirement."""
    password = input(f"Enter a password (at least {min_length} characters): ")
    while len(password) < min_length:
        print("Password too short, try again.")
        password = input(f"Enter a password (at least {min_length} characters): ")
    return password

def print_asterisks(password):
    """Print the password as asterisks only."""
    print('*' * len(password))

main()