#Дан список чисел, опеределите сколько в нем встречается различных чисел.

import random
n = int(input("введите количество элементов списка >"))
m = []
for num in range(0,n):
    random_num = round(random.randint(1,10))
    m.append(random_num)   
print (m)
a = set(m)
print (a)
