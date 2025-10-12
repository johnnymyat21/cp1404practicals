# CP1404 Practical 04 - Quick Pick Generator (basic loops only; no random.sample)

import random

NUMBERS_PER_PICK = 6
LOWEST = 1
HIGHEST = 45

count = int(input("How many quick picks? "))

for _ in range(count):
    pick = []
    while len(pick) < NUMBERS_PER_PICK:
        n = random.randint(LOWEST, HIGHEST)
        if n not in pick:            # no repeats
            pick.append(n)
    pick.sort()
    # format each number to width 2
    print(" ".join(f"{n:2d}" for n in pick))
