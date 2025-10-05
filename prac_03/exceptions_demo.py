"""CP1404 Practical 03 – Exceptions demo using specific handlers and validation loop."""


def main():
    try:
        numerator = int(input("Numerator: "))
        denominator = int(input("Denominator: "))

        # Input-validation loop pattern (avoid ZeroDivisionError before dividing)
        while denominator == 0:
            print("Cannot divide by zero; please enter a non-zero denominator.")
            denominator = int(input("Denominator: "))

        result = numerator / denominator
    except ValueError:
        print("Numerator and denominator must be valid integers.")
    else:
        # Runs only if try-suite had no exception
        print(f"{numerator} / {denominator} = {result}")
    finally:
        # Runs regardless; useful for clean-up (nothing to clean here, just a demo)
        print("Finished.")


if __name__ == "__main__":
    main()

# Q1: ValueError occurs when non-integers are entered (e.g., 'abc').
# Q2: ZeroDivisionError occurs if attempting division with denominator == 0 (but we prevent it).
# Q3: Yes—use the validation loop (as above) to ensure denominator != 0 before division.
