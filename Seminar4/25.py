""" Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 """

newtext = 'a a a b c a a d c d d'
newtext2 = newtext.split()

data = {}
res = ''

for item in newtext2:
    if item in data:
        data[item] += 1
        res += item + '_' + str(data[item]) + ' '
    else:
        data[item] = 0
        res += item + ' '
print(res)
