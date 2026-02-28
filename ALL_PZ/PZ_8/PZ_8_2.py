# Задание: Сгенерировать словарь вида {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36},
# удалить из него второй и третий элементы. Отобразить исходный и получившийся словарь.
# Использовать for, range.


square_dict = {}
for i in range(7):
    square_dict[i] = i ** 2

print("Исходный словарь:", square_dict)

keys_to_remove = [1, 2]
for key in keys_to_remove:
    del square_dict[key]

print("Словарь после удаления 2-го и 3-го элементов:", square_dict)
