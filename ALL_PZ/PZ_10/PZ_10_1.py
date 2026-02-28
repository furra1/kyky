# -*- coding: utf-8 -*-
"""
ПЗ № 10, Вариант 15, Задание 1
Обработка числового файла: индекс последнего мин. элемента, умножение на первый
"""

import random

numbers = [random.randint(-100, 100) for _ in range(15)]
with open('data_15.txt', 'w') as f:
    f.write(' '.join(map(str, numbers)))

with open('data_15.txt') as f:
    data = [int(x) for x in f.read().split()]

count = len(data)
min_val = min(data)
last_min_idx = len(data) - 1 - data[::-1].index(min_val)
first_elem = data[0]
multiplied = [x * first_elem for x in data]

with open('result_15.txt', 'w') as f:
    f.write("Исходные данные:\n")
    f.write(' '.join(map(str, data)) + '\n')
    f.write("Количество элементов: " + str(count) + '\n')
    f.write("Индекс последнего минимального элемента: " + str(last_min_idx) + '\n')
    f.write("Умножаем все элементы на первый элемент: " + ' '.join(map(str, multiplied)) + '\n')

print("Исходные данные:", data)
print("Количество элементов:", count)
print("Индекс последнего минимального элемента:", last_min_idx)
print("Результат записан в result_15.txt")
