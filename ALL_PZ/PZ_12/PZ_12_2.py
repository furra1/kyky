# Задание (вариант 15): В матрице найти минимальный элемент в предпоследней строке.

matrix = [
    [12, 5, -3, 8],
    [1, 9, 4, 2],
    [6, -7, 0, 11],
    [3, 14, -2, 5],
]

print("Исходная матрица:")
for row in matrix:
    print(row)

penultimate_row = matrix[-2]
min_value = min(penultimate_row)
min_index = penultimate_row.index(min_value)

print(f"\nПредпоследняя строка: {penultimate_row}")
print(f"Минимальный элемент: {min_value} (индекс {min_index})")
