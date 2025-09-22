"""Temperature conversions with pure functions and a menu."""


def main():
    """Run the temperature conversion menu."""
    menu = "(C)elsius to Fahrenheit\n(F)ahrenheit to Celsius\n(Q)uit"
    print(menu)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "C":
            celsius = get_float("Celsius: ")
            print(f"Result: {celsius_to_fahrenheit(celsius):.2f} F")
        elif choice == "F":
            fahrenheit = get_float("Fahrenheit: ")
            print(f"Result: {fahrenheit_to_celsius(fahrenheit):.2f} C")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").strip().upper()
    print("Thank you. Bye!")


def get_float(prompt):
    """Get a valid float from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number; try again.")


def celsius_to_fahrenheit(celsius):
    """Return Fahrenheit converted from the given Celsius."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Return Celsius converted from the given Fahrenheit."""
    return (fahrenheit - 32) * 5 / 9


main()
