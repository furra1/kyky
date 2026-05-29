# Задание (вариант 15): В матрице найти суммы элементов каждого столбца и поместить их
# в новый массив. Выполнить замену элементов второй строки исходной матрицы
# на полученные суммы.

matrix = [
    [2, -1, 4, 0],
    [5, 3, -2, 1],
    [7, 6, 1, 8],
    [-3, 2, 4, 5],
]

print("Исходная матрица:")
for row in matrix:
    print(row)

col_sums = [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
print("\nСуммы по столбцам:", col_sums)

matrix[1] = col_sums

print("\nМатрица после замены второй строки:")
for row in matrix:
    print(row)
