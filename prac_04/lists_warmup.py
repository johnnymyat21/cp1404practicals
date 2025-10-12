# CP1404 Practical 04 - Lists Warm-Up (simple)

numbers = [3, 1, 4, 1, 5, 9, 2]

# Predict (write answers first, then run to check):
# numbers[0] -> 3
# numbers[-1] -> 2
# numbers[3] -> 1
# numbers[:-1] -> [3, 1, 4, 1, 5, 9]
# numbers[3:4] -> [1]
# 5 in numbers -> True
# 7 in numbers -> False
# "3" in numbers -> False
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Required statements
numbers[0] = "ten"   # string, not 10
numbers[-1] = 1
print(numbers[2:])    # all except first two
print(9 in numbers)   # True/False
