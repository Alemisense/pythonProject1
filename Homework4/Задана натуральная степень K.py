# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


import random
import os

k = int(input('Введите степень: '))

polynomial = ""
while k >= 0:
    coeff = random.randint(0, 100)
    if coeff != 0:
        match k:
            case 1: polynomial += (str(coeff) + "*x" + " + ")
            case 0: polynomial += (str(coeff) + " = 0")
            case _: polynomial += (str(coeff) + "*x^" + str(k) + " + ")
    k -= 1
print(polynomial)

path = os.path.join('File.txt')
with open(path, 'w') as data:
    data.write(polynomial)