from random import randrange

def rand_num(count):
    if count < 0:
        print("Некорректное число")
        return []
    arr = []
    for i in range(count):
        arr.append(randrange(count))
    return arr

def new_lst(num):
    new_arr = []
    [new_arr.append(i) for i in num if i not in new_arr]
    return new_arr

n = int(input("Введите число: "))
array = rand_num(n)
print(array)
lst = new_lst(array)
print(lst)