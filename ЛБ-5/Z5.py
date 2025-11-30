import random
import string

def generate_random_string(length: int) -> str:
    """Генерирует случайную строку из букв ASCII и цифр."""
    # Определяем набор символов, из которых будет состоять строка
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    
    # Генерируем строку
    random_string = ''.join(random.choice(characters) for i in range(length))
    
    return random_string

# 1. Пользователь вводит сообщение
message = input("Введите сообщение: ")

# 2. Пользователь вводит количество подстановочных символов
n = int(input("Введите количество подстановочных символов: "))

# 3. К каждой букве добавляем n рандомных букв и объединяем в одно сообщение
encoded_message = ""

for char in message:
    # Добавляем исходный символ
    encoded_message += char
    # Добавляем n случайных символов после каждого исходного символа
    encoded_message += generate_random_string(n)

# 4. Выводим полученное кодированное послание
print("\nЗакодированное сообщение:")
print(encoded_message)