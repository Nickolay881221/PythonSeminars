""" Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
Заполните массив случайными натуральными числами от 1 до N/2.
Выведите, сколько раз X встречается в массиве.

Ввод: 5
Ввод: 1

1 2 1 2 2
Вывод: 2 """


import random
n = int(input("введите количество количество элементов массива >"))
x = int(input("введите число необходимое для проверки >"))
m = []
for num in range(0, n):
    random_num = round(random.randint(1, n//2))
    m.append(random_num)
print(m)
count = 0
for i in range(0,len(m)):
    if m[i] == x:
        count += 1
print(count)