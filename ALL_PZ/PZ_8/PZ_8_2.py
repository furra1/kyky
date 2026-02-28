# -*- coding: utf-8 -*-
"""
ПЗ № 8, Вариант 15, Задание 2
Словарь квадратов с удалением 2-го и 3-го элементов
"""

square_dict = {}
for i in range(7):
    square_dict[i] = i ** 2

print("Исходный словарь:", square_dict)

keys_to_remove = [1, 2]
for key in keys_to_remove:
    del square_dict[key]

print("Словарь после удаления 2-го и 3-го элементов:", square_dict)
