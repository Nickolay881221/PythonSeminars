import random

matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def showMatrix():
    print(matrix[0],matrix[1],matrix[2])
    print(matrix[3],matrix[4],matrix[5])
    print(matrix[6],matrix[7],matrix[8])


def checkWin():
    if matrix[0] == matrix[1] == matrix[2]:
        print(f'Победили {matrix[0]}')
        return 1
    elif matrix[3] == matrix[4] == matrix[5]:
        print(f'Победили {matrix[3]}')
        return 1
    elif matrix[6] == matrix[7] == matrix[8]:
        print(f'Победили {matrix[6]}')
        return 1
    elif matrix[0] == matrix[3] == matrix[6]:
        print(f'Победили {matrix[0]}')
        return 1
    elif matrix[1] == matrix[4] == matrix[7]:
        print(f'Победили {matrix[1]}')
        return 1
    elif matrix[2] == matrix[5] == matrix[8]:
        print(f'Победили {matrix[2]}')
        return 1
    elif matrix[0] == matrix[4] == matrix[8]:
        print(f'Победили {matrix[0]}')
        return 1
    elif matrix[2] == matrix[4] == matrix[6]:
        print(f'Победили {matrix[2]}')
        return 1
    else:
        return 0

matrix = ['x', 'x', 3, 4, 5, 6, 7, 8, 9]

showMatrix()

def player():
    while True:
        try:
            number = int(input('Введите ночер ячейки, чтобы поставить крестик: '))
            if (matrix[number-1] != 'x') and matrix[number-1] != 'o':
                matrix[number-1] = 'x'
                break
            else:
                print("Неверный ввод. Ячейка занята")
        except:
            print("неверный ввод")    


def comp(matrix):
    for i in range(0, len(matrix)):
        if (matrix[i] != 'x') and matrix[i] != 'o':
            matrix[i] = 'o'
            return
showMatrix()

while True:
    
    player()
    showMatrix()
    if checkWin() == 1:
        break
    comp(matrix)
    showMatrix()
    if checkWin() == 1:
        break



showMatrix()
checkWin()
comp(matrix)
showMatrix()
comp(matrix)
showMatrix()