
""" def factorial(n):
    result = int(1)
    while n > 0:
        result *= n
        n -= 1
    return result
n = int(input('Введите число >'))
print(f"факториал введенного числа равен {factorial(n)}") """


""" def fibonachi(n):
    a = 0
    b = 1
    c = 0
    d = 2
    while c < n:
        c = a + b
        a = b
        b = c
        d += 1
    if c == n:
        print(f"введенное число является {d} числом в последовательности фибонначи")
    else:
        print(-1)
n = int(input("введите необходимое число >"))
fibonachi(n) """

""" Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, 
в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50 """

""" import random

n = 100
m = []
countDay = 0
maxDay = 0
count = 0
for num in range(0,n):
    random_num = round(random.randint(-50,50))
    m.append(random_num)    
print(n)
print(m)
for x in m:
    if x > 0:
        count += 1
    else:
        if maxDay < count:
            maxDay = count
        count = 0
    if maxDay < count:
        maxDay = count
print(maxDay)
 """
import random
n = int(input("введите количество арбузов>"))
m = []
for num in range(0,n):
    random_num = round(random.randint(1,30000))
    print(random_num)   
    m.append(random_num)   
min = 35000
max = 0
for x in m:
    if x < min: min = x
    if x > max: max = x
print(min, max)



