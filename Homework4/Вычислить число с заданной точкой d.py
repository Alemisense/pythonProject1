# Вычислить число c заданной точностью d

import math

def get_count(number: float):
    count = 0
    while number != 1:
        number *= 10
        count += 1
    return count

d = float(input('Введите точность : '))
c = get_count(d)
pi_str = str(math.pi)
e = 2 + c
print(f'- при d = {d}, π = ', pi_str[0:e])