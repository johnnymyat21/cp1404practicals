"""
Hex Colours
Estimate: 20 minutes
Actual:   (fill in after you finish)
"""
# Store keys in lowercase to make lookups case-insensitive
NAME_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "beige": "#f5f5dc",
    "black": "#000000",
    "blueviolet": "#8a2be2",
    "coral": "#ff7f50",
    "crimson": "#dc143c",
    "darkgreen": "#006400",
    "gold": "#ffd700",
    "indigo": "#4b0082",
}

def main():
    print("Look up hex colour codes (blank to quit)")
    while True:
        name = input("Colour name: ").strip().lower()
        if not name:
            break
        code = NAME_TO_HEX.get(name)
        if code:
            print(code)
        else:
            print("Invalid colour name")

if __name__ == "__main__":
    main()
