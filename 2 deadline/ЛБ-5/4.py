text = input("Текст: ").lower()

words = set(text.split())

print(f"Уникальных слов: {len(words)}")

long = {w for w in words if len(w) > 5}
print(f"Слова длиннее 5 букв: {long}")

key_words = {"python", "programming"}
found = key_words & words 
print(f"Найдены слова: {bool(found)}")