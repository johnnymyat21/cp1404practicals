# CP1404 Practical 04 - Total Income (basic, procedural)

print("How many months? ", end="")
month_count = int(input())
print()

incomes = []
for month in range(1, month_count + 1):
    income = float(input(f"Enter income for month {month}: "))
    incomes.append(income)

print()
print("Income Report")
print("-------------")
running_total = 0
for month in range(1, month_count + 1):
    running_total += incomes[month - 1]
    print(f"Month {month:2} - Income: ${incomes[month - 1]:10.2f}  "
          f"Total: ${running_total:10.2f}")
