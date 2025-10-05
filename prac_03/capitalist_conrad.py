"""CP1404 Practical 03 – Capitalist Conrad: volatile price simulator with file output."""
import random

# Constants (ALL_CAPS) as per style & readability guidance
MIN_PRICE = 1.00
MAX_PRICE = 100.00
MAX_INCREASE = 0.175  # up to 17.5%
MAX_DECREASE = 0.05  # up to 5%
INITIAL_PRICE = 10.00
FILENAME = "conrad_prices.txt"


def simulate_until_bounds(start_price):
    """Return list of daily prices (excluding the starting line) until out of bounds."""
    prices = []
    price = start_price
    while MIN_PRICE <= price <= MAX_PRICE:  # standard indefinite while pattern
        if random.randint(1, 2) == 1:  # 50/50
            price *= (1 + random.uniform(0, MAX_INCREASE))
        else:
            price *= (1 - random.uniform(0, MAX_DECREASE))
        prices.append(price)
    return prices


def write_prices(filename, start_price, prices):
    """Write starting price and each day’s price to file, one per line with day number."""
    with open(filename, "w") as out_file:  # use with to ensure close()
        print(f"Starting price: ${start_price:,.2f}", file=out_file)
        for day_number, price in enumerate(prices, start=1):
            print(f"On day {day_number} price is: ${price:,.2f}", file=out_file)


def main():
    print(f"Starting price: ${INITIAL_PRICE:,.2f}")
    daily_prices = simulate_until_bounds(INITIAL_PRICE)
    # Also echo to screen in the same format:
    for i, p in enumerate(daily_prices, start=1):
        print(f"On day {i} price is: ${p:,.2f}")
    write_prices(FILENAME, INITIAL_PRICE, daily_prices)


if __name__ == "__main__":
    main()
