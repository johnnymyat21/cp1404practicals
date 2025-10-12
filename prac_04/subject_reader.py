# CP1404 Practical 04 - Subject Reader (simple split/join style)

FILENAME = "subject_data.txt"

subjects = []  # will become a list of [code, lecturer, students]
in_file = open(FILENAME, "r", encoding="utf-8")
for line in in_file:
    parts = line.strip().split(",")     # ['CP1401','Ada Lovelace','192']
    parts[2] = int(parts[2])            # convert student count to int
    subjects.append(parts)
in_file.close()

# Display results
for subject in subjects:
    code = subject[0]
    lecturer = subject[1]
    students = subject[2]
    print(f"{code} is taught by {lecturer} and has {students:3d} students")
