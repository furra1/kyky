# Задание (вариант 15): В матрице найти суммы элементов каждого столбца и поместить их
# в новый массив. Выполнить замену элементов второй строки исходной матрицы
# на полученные суммы.

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

matrix = [[random.randint(-9, 9) for _ in range(cols)] for _ in range(rows)]

print('\nИсходная матрица (сгенерирована):')
for row in matrix:
    print(row)

col_sums = [sum(matrix[i][j] for i in range(rows)) for j in range(cols)]
print('\nСуммы по столбцам:', col_sums)

matrix[1] = col_sums

print('\nМатрица после замены второй строки:')
for row in matrix:
    print(row)
