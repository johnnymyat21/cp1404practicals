"""CP1404 Practical 03 – Password checker (length + digit/lower/upper [+ optional special])."""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def print_requirements():
    """Print the current password rules using the constants."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("    1 or more uppercase characters")
    print("    1 or more lowercase characters")
    print("    1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print(f"    and 1 or more special characters:  {SPECIAL_CHARACTERS}")


def is_valid_password(password):
    """Return True if password meets the configured rules; otherwise False."""
    if not (MIN_LENGTH <= len(password) <= MAX_LENGTH):
        return False

    count_lower = count_upper = count_digit = count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_lower < 1 or count_upper < 1 or count_digit < 1:
        return False
    if SPECIAL_CHARS_REQUIRED and count_special < 1:
        return False
    return True


def main():
    print_requirements()
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)} character password is valid: {password}")


if __name__ == "__main__":
    main()
