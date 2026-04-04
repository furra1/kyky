# Задание: Составить генератор (yield), который выводит из строки только буквы.


def letters_only(text):
    """Генератор, возвращающий только буквенные символы из строки."""
    for char in text:
        if char.isalpha():
            yield char


test_string = "Hello, World! 123"
print("Исходная строка:", test_string)
print("Только буквы:", list(letters_only(test_string))) 
""" сделать без lista, и скомновать"""
