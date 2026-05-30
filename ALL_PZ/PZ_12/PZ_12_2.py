# Задание (вариант 15): В матрице найти минимальный элемент в предпоследней строке.

import random

ROWS, COLS = 4, 4
matrix = [[random.randint(-20, 20) for _ in range(COLS)] for _ in range(ROWS)]

print("Исходная матрица (сгенерирована):")
for row in matrix:
    print(row)

penultimate_row = matrix[-2]
min_value = min(penultimate_row)
min_index = penultimate_row.index(min_value)

print(f"\nПредпоследняя строка: {penultimate_row}")
print(f"Минимальный элемент: {min_value} (индекс {min_index})")
