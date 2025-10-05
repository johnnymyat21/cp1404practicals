"""CP1404 Practical 03 – String formatting & aligned output."""


def print_guitar_line():
    """Print '1922 Gibson L-5 CES for about $16,036!' using f-string formatting."""
    year = 1922
    guitar = "Gibson L-5 CES"
    price = 16035.99
    print(f"{year} {guitar} for about ${price:,.0f}!")


def print_powers_of_two():
    """Print 2^i table with right-aligned integers like the sample."""
    for i in range(11):  # 0..10
        print(f"2 ^ {i:>2} is {2 ** i:>5}")


def main():
    print_guitar_line()
    print_powers_of_two()


if __name__ == "__main__":
    main()
