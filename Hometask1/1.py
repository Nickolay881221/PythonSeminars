# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input('Введите трехзначное число >'))

b = int(a % 10+(a//10) % 10+(a//100) % 10)

print(b)