n = int(input("Введите число n: "))

total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"Сумма чисел от 1 до {n}: {total_sum}")