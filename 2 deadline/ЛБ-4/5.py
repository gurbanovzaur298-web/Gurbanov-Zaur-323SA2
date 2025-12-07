import re
from collections import Counter

print("Введите текст (пустая строка для завершения):")
lines = []
while True:
    try:
        line = input()
        if line == "":
            break
        lines.append(line)
    except EOFError:
        break

text = " ".join(lines)

clean_text = re.sub(r'[^\w\s]', '', text.lower())

words = clean_text.split()

if not words:
    print("Текст не содержит слов!")
else:

    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    
    avg_length = sum(len(word) for word in words) / len(words)
    
    word_counts = Counter(words)
    top_5_words = word_counts.most_common(5)
    
print(f"\nСамое длинное слово: {longest_word}")
print(f"Самое короткое слово: {shortest_word}")
print(f"Средняя длина: {average_length:.1f}")
print(f"Топ-5 слов: {top_words}")
