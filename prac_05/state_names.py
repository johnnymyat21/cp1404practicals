"""
State Names
Estimate: 15 minutes
Actual:   (fill in after you finish)
"""
STATE_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "SA": "South Australia",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "ACT": "Australian Capital Territory",
}

def main():
    print("Enter short state names to look up (blank to stop)")
    while True:
        state = input("State: ").strip()
        if not state:
            break
        key = state.upper()  # accept lowercase inputs as well
        try:
            print(f"{key} is {STATE_NAMES[key]}")
        except KeyError:
            print("Invalid short state")

    print()
    # Neatly print all states and names, aligned
    width = max(len(k) for k in STATE_NAMES)
    for abbr, name in STATE_NAMES.items():
        print(f"{abbr:{width}} is {name}")

if __name__ == "__main__":
    main()
