"""CP1404 Practical 03 – Files (read/write with different techniques)."""

# 1. Ask for name, write to name.txt (use open/close)
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)          # using print with file=...
out_file.close()

# 2. Read the name and greet (use open/close)
in_file = open("name.txt", "r")
saved_name = in_file.read().strip()  # strip() removes the trailing newline
in_file.close()
print(f"Hi {saved_name}!")

# 3. Read only the first two numbers from numbers.txt, print their sum (use with)
with open("numbers.txt", "r") as f:
    first = int(f.readline())
    second = int(f.readline())
print(first + second)               # should be 59 for the given file

# 4. Print the total for ALL lines in numbers.txt (use with + for line in file)
total = 0
with open("numbers.txt", "r") as f:
    for line in f:                  # definite iteration over lines
        total += int(line.strip())
print(total)
