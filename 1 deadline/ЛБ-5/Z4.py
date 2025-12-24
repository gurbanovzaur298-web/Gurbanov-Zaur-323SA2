# 1. Пользователь вводит 5 чисел
numbers = input("Введите 5 чисел через пробел: ").split()

# Преобразуем введенные строки в числа
num1, num2, num3, num4, num5 = map(int, numbers)

# 2. Находим минимальное и максимальное значение
min_number = min(num1, num2, num3, num4, num5)
max_number = max(num1, num2, num3, num4, num5)

# 3. Выводим результаты
print("Минимальное число:", min_number)
print("Максимальное число:", max_number)