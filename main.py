from collections import Counter

text = input("Введите текст: ").lower()
letter_count = Counter(char for char in text if char.isalpha())

for letter, count in sorted(letter_count.items()):
    print(f"Буква '{letter}': {count} раз(а)")

text = input("Введите текст: ")
count = 0

for char in text:
    if char.isupper():  # проверяем, является ли символ заглавной буквой
        count += 1

print(f"Количество заглавных букв в тексте: {count}")