text = input("Введите текст: ")

step = int(input("Введите шаг: "))

result = text[::step]

print("\nТекст с шагом", step, ":")
print(result)