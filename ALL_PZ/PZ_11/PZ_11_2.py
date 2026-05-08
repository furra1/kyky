# Задание: Составить генератор (yield), который выводит из строки только буквы.

test_string = "Hello, World! 123"

def extract_letters(text):
    """Функция-генератор, возвращающая только буквы."""
    for char in text:
        if char.isalpha():
            yield char
            
gen = extract_letters(test_string)
result = "".join(gen)

print("Исходная строка:", test_string)
print("Только буквы:", result)
