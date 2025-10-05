"""CP1404 Practical 03 – Exceptions To Complete (robust integer input + safe division)."""


def main():
    valid_input = False
    while not valid_input:  # validation-loop pattern
        try:
            numerator = int(input("Enter the numerator (int): "))
            denominator = int(input("Enter the denominator (int): "))
            while denominator == 0:  # guard against /0
                print("Denominator cannot be 0. Please enter a non-zero integer.")
                denominator = int(input("Enter the denominator (int): "))
            result = numerator / denominator
            valid_input = True
        except ValueError:
            print("Please enter valid integers.")

    print(f"Result is {result}")


if __name__ == "__main__":
    main()
