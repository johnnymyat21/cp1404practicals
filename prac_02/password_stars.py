"""Password stars with functions."""
MIN_LENGTH = 4  # constant is OK


def main():
    """Get a valid password then print stars equal to its length."""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    """Get a password that meets the required minimum length; return it."""
    password = input("Password: ")
    while len(password) < min_length:
        print(f"Password too short; minimum is {min_length}.")
        password = input("Password: ")
    return password


def print_asterisks(text, symbol="*"):
    """Print symbols equal to the length of the given text."""
    print(symbol * len(text))


main()
