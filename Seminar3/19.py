#Дана последовательность из чисел и число k. Необходимо сдвинуть всю последовательность на k элементов вправо
# (сдвиг циклический). k - положительное число.

import random
n = int(input("введите количество количество элементов списка >"))
k = int(input("введите число для сдвига"))
m = []
for num in range(0,n):
    random_num = round(random.randint(1,10))
    m.append(random_num)   
print (m)
for i in range(0, k):
    t = m.pop(-1)
    m.insert(0,t)
print(m)