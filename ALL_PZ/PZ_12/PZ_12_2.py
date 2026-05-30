# Задание (вариант 15): В матрице найти минимальный элемент в предпоследней строке.

import random

while True:
    try:
        rows = int(input('Введите количество строк матрицы: '))
        cols = int(input('Введите количество столбцов матрицы: '))
        if rows < 2 or cols < 1:
            print('Нужно минимум 2 строки и 1 столбец.')
            continue
        break
    except ValueError:
        print('Введите целые числа.')

matrix = [[random.randint(-20, 20) for _ in range(cols)] for _ in range(rows)]

print('\nИсходная матрица (сгенерирована):')
for row in matrix:
    print(row)

penultimate_row = matrix[-2]
min_value = min(penultimate_row)
min_index = penultimate_row.index(min_value)

print(f'\nПредпоследняя строка: {penultimate_row}')
print(f'Минимальный элемент: {min_value} (индекс {min_index})')
