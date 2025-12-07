students = [
    ("Заур", 19, 4.5),
    ("Анатолий", 21, 4.2),
    ("Амир", 20, 4.8),
    ("Степан", 22, 4.0),
    ("Мачомед кызы", 19, 4.9)
]

print("Старше 20 лет:")
for student in students:
    if student[1] > 20:
        print(student[0])

best = students[0]
for student in students:
    if student[2] > best[2]:
        best = student
print(f"\nЛучший студент: {best[0]}")

print("\nОтсортированный список:")
sorted_students = sorted(students)
for student in sorted_students:
    print(f"{student[0]} - {student[2]}")
