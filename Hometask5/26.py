""" Задача 26:
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии. """

import random
a = int(input("введите число а >"))
b = int(input("введите число b, в которое будет возведено число a >"))

def multiplikate(a, b):
    if b>1:
        return a*multiplikate(a,b-1)
    else:
        return a

print(multiplikate(a,b))