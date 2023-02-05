""" Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.

Структура данных:
Фамилия, имя, отчество, номер телефона.

Пример данных:
Ivanov, Ivan, Ivanovich, +79111234567
Petrov, Petr, Petrovich, +79119876543

Функции справочника:
- Показать все записи
- Найти запись по вхождению частей имени
- Найти запись по телефону
- Добавить новый контакт
- Удалить контакт
- Изменить номер телефона у контакта
.
Пример работы программы:
.
При запуске программы пользователю выдается меню:

Введите номер действия:
1 - Показать все записи
2 - Найти запись по вхождению частей имени
3 - Найти запись по телефону
4 - Добавить новый контакт
5 - Удалить контакт
6 - Изменить номер телефона у контакта
7 - Выход """



fileName = 'telephone directory.txt'
""" функция отображения всех записей в словаре """
def ShowAll(fileName):
    result = []
    with open(fileName, "r+") as data:
        for object in data:
            result.append(object.split(","))
    for element in result:
        if element[3][-1:] == "\n":
            element[3] = element[3][:-1]
    return result

""" print(ShowAll(fileName)) """

def FindObject(data):
    name = input('Введите искомое имя >')
    for line in data:
        if line[1] == name:
            print(line)

""" FindObject(ShowAll(fileName)) """

def FindObjectForNumberFhone(data):
    number = input('Введите номер телефона в формате +71234567890>')
    for line in data:
        if line[3][:12] == number:
            print(line)

""" FindObjectForNumberFhone(ShowAll(fileName)) """

def addNewUser(fileName):
    family = input('Введите фамилию >')
    name = input('Введите имя >')
    patronymic = input('Введите отчество >')
    phonenumber = input('Введите номер телефона >')
    file = open(fileName, "a")
    file.write(f"\n{family},{name},{patronymic},{phonenumber}")
    file.close()
    print('новый пользователь добавлен')

""" addNewUser(fileName) """
""" print(ShowAll(fileName)) """

def delUser(data, fileName):
    delNumber = int(input('Введите порядковый номер записи справочника для удаления >'))
    
    del data[delNumber - 1]
    
    file = open(fileName, "w")
    for n in data:
        file.write(f"{n[0]},{n[1]},{n[2]},{n[3]}\n")
    file.close()

""" delUser(ShowAll(fileName), fileName) """
""" print(ShowAll(fileName)) """

def changeNumber(data, fileName):
    changeNumberId = int(input('Введите порядковый номер записи для изменения телефона >')) 
    changeNumber = int(input('Введите новый номер телефона >')) 
    data[changeNumberId-1][3] = changeNumber 
    file = open(fileName, "w")
    for n in data:
        file.write(f"{n[0]},{n[1]},{n[2]},{n[3]}\n")
    file.close()

""" changeNumber(ShowAll(fileName), fileName)
print(ShowAll(fileName)) """


def showMenu():
    with open("menu.txt", encoding='utf-8') as data:
        for line in data:
            print(line)
    choise = input("Введите желаемое действие >")
    match choise:
        case "1":
            print(ShowAll(fileName))
            showMenu()
        case "2":
            FindObject(ShowAll(fileName))
            showMenu()
        case "3":
            FindObjectForNumberFhone(ShowAll(fileName))
            showMenu()
        case "4":
            addNewUser(fileName)
            print(ShowAll(fileName))
            showMenu()
        case "5":
            delUser(ShowAll(fileName), fileName)
            print(ShowAll(fileName))
            showMenu()
        case "6":
            changeNumber(ShowAll(fileName), fileName)
            showMenu()
        case "7":
            print("Пока")


showMenu()

