""" Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной """

fileName = 'tel.txt'

def writeFile(file_name):
    with open(file_name, 'a') as data:
        data.writelines("Hello world" + '\n')

def readFile(file_name):
    result = []
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    return result

print(type(readFile(fileName)))
print(readFile(fileName))

def findUsers(userList):
    name = 'Ivan,'
    for user in userList:
        if user[1] == name:
            print(user[3])

findUsers(readFile(fileName))

""" import os
import time

def search_data():
pass

def output_data_string(data):
pass

def save_data_to_file(data):
pass

def print_all_data():
pass

def add_data():
pass

if __name__ == '__main__':
#основной длок
menu='''1 - Вывод данных\n2 - Добавление записи\n3 - Поиск\n4 - Выход'''
while (True):
os.system("cls")
print(menu)
answer = input('>:')
match answer:
case "1":
#вывод данных
print_all_data()
pass
case "2":
#добавление данных
add_data()
pass
case "3":
#поиск
search_data()
pass
case "4":
#выход
exit(0)
case _:
print("неверный ввод")
time.sleep(3) """