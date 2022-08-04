# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = 45

def decimal_to_binary(n):
    if (n > 1):
        decimal_to_binary(n // 2)
    print(n % 2, end='')

decimal_to_binary(n)
print()