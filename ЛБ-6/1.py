fio = input("Введите ФИО: ")
result = ' '.join(word.capitalize() for word in fio.split())
print(f"Добро пожаловать {result}")