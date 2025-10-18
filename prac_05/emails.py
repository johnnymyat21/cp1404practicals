"""
Emails
Estimate: 30 minutes
Actual:   (fill in after you finish)
"""
def extract_name(email: str) -> str:
    """Return a 'pretty' name guessed from an email address."""
    username = email.split('@', 1)[0]
    parts = username.replace('.', ' ').replace('_', ' ').split()
    return " ".join(parts).title() if parts else ""

def main():
    email_to_name = {}
    while True:
        email = input("Email: ").strip()
        if not email:
            break
        default_name = extract_name(email)
        confirmation = input(f"Is your name {default_name}? (Y/n) ").strip().lower()
        if confirmation not in {"", "y", "yes"}:
            name = input("Name: ").strip()
        else:
            name = default_name
        email_to_name[email] = name

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
