# CP1404 Practical 04 - Simple list comprehensions from slides

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["Ada", "Alan", "Grace", "Linus", "Guido", "Barbara", "Tim"]

# examples like the slides:
evens = [n for n in numbers if n % 2 == 0]
print(evens)

first_initials = [name[0] for name in names]
print(first_initials)

# filter by startswith (case-insensitive)
g_names = [name for name in names if name.lower().startswith("g")]
print(g_names)

# split then comprehension (strings are sequences too)
date_string = "13/11/1945"
parts = date_string.split("/")                 # ['13','11','1945']
dob_tuple = tuple([int(p) for p in parts])     # (13, 11, 1945)
print(dob_tuple)
