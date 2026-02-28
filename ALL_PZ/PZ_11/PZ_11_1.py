# Задание: В последовательности на n целых чисел найти и вывести:
# 1. максимальный среди положительных
# 2. минимальный среди отрицательных
# 3. произведение элементов


sequence = [5, -3, 8, -12, 2, -7, 15, 0, -1, 4]
print("Исходная последовательность:", sequence)

positive_nums = [x for x in sequence if x > 0]
max_positive = max(positive_nums) if positive_nums else None
print("Максимальный среди положительных:", max_positive)

negative_nums = [x for x in sequence if x < 0]
min_negative = min(negative_nums) if negative_nums else None
print("Минимальный среди отрицательных:", min_negative)

product = 1
for x in sequence:
    product *= x
print("Произведение элементов:", product)
