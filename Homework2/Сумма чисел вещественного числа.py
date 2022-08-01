# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


float_num = input('input float number: ')
sum = 0
for i in float_num:
    if i != '.':
        sum += int(i)
print(sum)