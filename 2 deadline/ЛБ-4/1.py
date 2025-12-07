grades = []

grades.append(4)
grades.append(5)
grades.append(3)
grades.append(2)
grades.append(4)

print(f"Текущие оценки: {grades}")

first_grade = grades.pop(0)  
last_grade = grades.pop()    

if grades: 
    average_grade = sum(grades) / len(grades)
    print(f"Средний балл: {average_grade:.2f}")
else:
    print("Список оценок пуст")

print(f"Итоговые оценки: {grades}")