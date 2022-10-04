# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('Введите число: '))
num = []
for i in range (1, n + 1):
    num.append(round((1 + 1/i)**i, 2))
print(num)
sum = 0
for i in num:
    sum += i
print("Сумма чисел в списке: ", sum)