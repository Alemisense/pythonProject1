# Задаа № 2
# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x = int(input("введите  число x - "))
y = int(input("введите  число y - "))


if (x > 0 and y > 0):
    print('точка находится в I четверти')
elif (x > 0 and y < 0):
    print('точка находится во II четверти')
elif (x < 0 and y < 0):
    print('точка находится в III четверти')
elif (x < 0 and y > 0):
    print('точка находится в IV четверти')
elif (x == 0 and y > 0):
    print('точка находится на оси y')
elif (x < 0 and y == 0):
    print('точка находится на оси x')
else:
    print('точка в центре')


