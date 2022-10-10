# 1. Вычислить число c заданной точностью d

from decimal import Decimal

def dip(n, d):
    num = Decimal(f"{n}")
    return num.quantize(Decimal(f"{d}"))

number = input("Введите число: ")
diap = input("Введите диапазон: ")
x = dip(number, diap)
print(x)