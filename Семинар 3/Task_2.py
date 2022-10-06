# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample


def num_in_list(count):
    if count < 0:
        print("Некорректное число")
        return []
    num = sample(range(1, count * 2), count)
    return num

def comp_nums(num_in_list):
    comp_list = []
    len_list = len(num_in_list)
    for i in range(len_list // 2):
        comp_list.append(num_in_list[i] * num_in_list[len_list - i - 1])
    if len_list % 2:
        comp_list.append(num_in_list[len_list // 2])
    return comp_list


count = int(input("Введите длину списка: "))
array = num_in_list(count)
print(array)
print(comp_nums(array))