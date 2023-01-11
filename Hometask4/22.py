""" Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого набора.
m - кол-во элементов второго набора.
Значения генерируются случайным образом.

Input: 11 6
(значения сгенерированы случайным образом
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18)

Output: 11 6
6 12 """

import random
n = int(input("введите количество количество элементов первого списка >"))
m = int(input("введите количество количество элементов второго списка >"))
k = []
l = []

def random_list(count):
    newlist = []
    for num in range(0, count):
        random_num = round(random.randint(1, 10))
        newlist.append(random_num)
    return newlist

k = random_list(n)
l = random_list(m)
print(k)
print(l)
res = []
for item in k:
    if item in l and item not in res:
        res.append(item)
        
print(sorted(res))

