numbers = input("Введите 5 чисел через пробел: ").split()

num1, num2, num3, num4, num5 = map(int, numbers)

min_number = min(num1, num2, num3, num4, num5)
max_number = max(num1, num2, num3, num4, num5)

print("Минимальное число:", min_number)

print("Максимальное число:", max_number)
