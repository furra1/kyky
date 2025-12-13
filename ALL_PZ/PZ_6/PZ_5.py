# Вариант 15
# 1. Составить функцию, которая выведет на экран строку, содержащую задаваемое с
# клавиатуры число символов
# 2. Дан прямоугольник, длины сторон которого равны натуральным числам А и В.
# Составить функцию, которая будет находить на сколько квадратов можно разрезать
# данный прямоугольник, если от него каждый раз отрезать квадрат наибольшей
# площади
#1
def print_line(length):
    try:
        if length < 0:
            print("Ошибка: Длина строки не может быть отрицательной.")
            return

        line = "*" * length
        print(f"Строка ({length} символов):")
        print(line)

    except TypeError:
        print("Ошибка ввода: Значение должно быть целым числом.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

try:
    N = input("Введите желаемое количество символов (целое число): ")
    
    N_int = int(N)
    print_line(N_int)
except ValueError:
    print("Ошибка: Введенное значение не является целым числом.")
except Exception as e:
    print_line("Ошибка")


#2
def count_squares(A, B):
    try:
        if A <= 0 or B <= 0:
            print("Ошибка: Длины сторон должны быть натуральными числами (> 0).")
            return 0
        count = 0 
        while A > 0 and B > 0:
            if A > B:
                num_squares = A // B
                count += num_squares
                A = A % B     
            else:
                num_squares = B // A
                count += num_squares
                B = B % A       
        return count

    except TypeError:
        print("Ошибка данных: Стороны A и B должны быть числами.")
        return 0
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return 0
