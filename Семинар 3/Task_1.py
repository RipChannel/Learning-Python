# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample


def num_in_list(count):
    if count < 0:
        print("Некорректное число")
        return []
    num = sample(range(1, count * 2), count)
    return num


def sum_in_list(num):
    sum = 0
    for i in range(0, len(num), 2):
        sum += num[i]
    return sum


count = int(input("Введите длину списка: "))
array = num_in_list(count)
print(array)
print(sum_in_list(array))