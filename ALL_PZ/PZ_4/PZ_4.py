# 1. Дано вещественное число A и целое число N (>0). Используя один цикл, найти сумму
# 1 + A + A2 + A3 + ... + AN.
# 2. Дано целое число N (>0), являющееся некоторой степенью числа 2: N = 2K.
# Найти целое число K — показатель этой степени.
#1
while True:
    try:
        a = int(input('Введите любое число! '))
        k = int(input('Введите степень этого числа '))
        if k <= 0:
            print('Введите целое число и не 0 ')
        break
    except (TypeError, ValueError)as e:
        print(f'Ошибка {e}')
        print('Введите корректные данные ')
summ = 1
for i in range(1,k+1):
summ += a ** i
print(summ)

#2
import math 
while True:
    try:
        n = int(input('Введите целое число больше 0 которое будет некоторой степенью числа 2: '))
        break
    except (TypeError, ValueError) as e:
        print(f'{e} Введите корректные данные')
logorifm = math.log(n,2)
print(logorifm)
