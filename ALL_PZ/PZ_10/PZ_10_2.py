# -*- coding: utf-8 -*-
"""
ПЗ № 10, Вариант 15, Задание 2
Обработка text18-15.txt: буквы в нижнем регистре, замена на верхний
"""

try:
    with open('text18-15.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    sample_text = """Зимний вечер
Буря мглою небо кроет,
Вихри снежные крутя.
То как зверь она завоет,
То заплачет как дитя."""
    with open('text18-15.txt', 'w', encoding='utf-8') as f:
        f.write(sample_text)
    content = sample_text

print("Содержимое файла:")
print(content)

lower_count = sum(1 for c in content if c.isalpha() and c.islower())
print("\nКоличество букв в нижнем регистре:", lower_count)

new_content = content.upper()
with open('result_text18-15.txt', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Текст записан в result_text18-15.txt")
