# Задание (вариант 15): В матрице найти суммы элементов каждого столбца и поместить их
# в новый массив. Выполнить замену элементов второй строки исходной матрицы
# на полученные суммы.

import random

ROWS, COLS = 4, 4
matrix = [[random.randint(-9, 9) for _ in range(COLS)] for _ in range(ROWS)]

print("Исходная матрица (сгенерирована):")
for row in matrix:
    print(row)

col_sums = [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
print("\nСуммы по столбцам:", col_sums)

matrix[1] = col_sums

print("\nМатрица после замены второй строки:")
for row in matrix:
    print(row)
