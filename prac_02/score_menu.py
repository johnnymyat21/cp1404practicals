"""Menu-driven score program that reuses determine_result()."""
from score import determine_result


def main():
    """Run the score menu loop."""
    score = get_valid_score()
    menu = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(menu)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_result(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").strip().upper()
    print("Farewell.")


def get_valid_score():
    """Get a score in the inclusive range 0–100."""
    while True:
        try:
            value = float(input("Score (0-100): "))
            if 0 <= value <= 100:
                return value
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid number; try again.")


main()
