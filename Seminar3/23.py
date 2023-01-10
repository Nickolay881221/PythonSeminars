# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)


import random
n = int(input("введите количество количество элементов списка >"))
m = []
for num in range(0, n):
    random_num = round(random.randint(1, 10))
    m.append(random_num)
print(m)
count = 0
for i in range(1, len(m)):
    if m[i-1] < m[i]:
        count += 1
print(count)
