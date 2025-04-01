from collections import Counter

text = input("Введите текст: ").lower()
letter_count = Counter(char for char in text if char.isalpha())

for letter, count in sorted(letter_count.items()):
    print(f"Буква '{letter}': {count} раз(а)")