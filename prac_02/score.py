"""Score classification using SRP and a random demo."""
import random


def main():
    """Get a valid score, print its result, then show a random example."""
    score = get_valid_score()
    print(determine_result(score))
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score} -> {determine_result(random_score)}")


def get_valid_score():
    """Get a score in the inclusive range 0–100."""
    while True:
        try:
            score = float(input("Score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid number; try again.")


def determine_result(score):
    """Return 'Bad' (<50), 'Passable' (50–89.99), or 'Excellent' (90–100)."""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
