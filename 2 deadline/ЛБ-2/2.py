n = int(input("Введите число для таблицы умножения: "))

print(f"Таблица умножения для числа {n}:")
print("-" * 20)

for i in range(1, 11):
    result = n * i
    print(f"{n} * {i} = {result}")