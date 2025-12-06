text = input("Введите текст: ")

word = input("Введите слово для поиска: ")

count = text.count(word)
first_index = text.find(word)  # возвращает -1 если слово не найдено

print(f"\nКоличество встреченных слов '{word}': {count}")

if first_index != -1:
    print(f"Индекс первого вхождения (с 0): {first_index}")
else:
    print("Слово не найдено в тексте")

text_without_word = text.replace(word, "")
print(f"\nТекст без слова '{word}':")
print(text_without_word)