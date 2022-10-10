# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def nums(n):
    arr = []
    d = 2
    while n > 1:
        if n % d == 0:
            arr.append(d)
            n //= d
        else:
            d += 1
    return arr


num = int(input("Введите натуральное число: "))
N = nums(num)
print(N)