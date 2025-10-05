"""CP1404 Practical 03 – Random numbers exploration."""
import random  # import first, then qualify as random.something (Functions slides)


def main():
    print(random.randint(5, 20))  # line 1: inclusive ends
    print(random.randrange(3, 10, 2))  # line 2: picks from 3,5,7,9
    print(random.uniform(2.5, 5.5))  # line 3: float in [2.5, 5.5]

    # Required: a random integer between 1 and 100 inclusive:
    print(random.randint(1, 100))


if __name__ == "__main__":
    main()

# Answers (based on function behaviour):
# Line 1 randint(5, 20): smallest 5, largest 20, integers only, both endpoints possible.
# Line 2 randrange(3, 10, 2): smallest 3, largest 9, set {3,5,7,9}. Could it be 4? No.
# Line 3 uniform(2.5, 5.5): float in [2.5, 5.5] (theoretically inclusive).
