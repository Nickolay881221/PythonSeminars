import random

class Mygame():
    def __init__(self):
        self.playField = [1,2,3,4,5,6,7,8,9]


    def playground(dataPlay): 
        for item in range(0,len(dataPlay),3):
            print("_"*13)
            print(f"| {dataPlay[item]} | {dataPlay[item+1]} | {dataPlay[item+2]} |")
        print("_"*13)
    
    def playerstep():
        step = int(input('введите номер клетки для хода >'))
        return step

    def checkPlaygroud(dataPlay, stepPlayer):
        for item in range(len(dataPlay)):
            if dataPlay[item] == stepPlayer:
                dataPlay[item] = "X"
        return dataPlay

    def AIstep(dataPlay):
        print("Ход противника:")
        possibleStep = []
        for item in range(len(dataPlay)):
            if dataPlay[item] != 'X' and dataPlay[item] != 'O':
                possibleStep.append(dataPlay[item])
        choice = random.choice(possibleStep)
        for item in range(len(dataPlay)):
            if dataPlay[item] == choice:
                dataPlay[item] = "O"
        return dataPlay

    def winner(dataPlay):
        if dataPlay[0] == dataPlay[1] == dataPlay [2]:
            print(f'Победили {dataPlay[0]}')
            return False
        if dataPlay[3] == dataPlay[4] == dataPlay [5]:
            print(f'Победили {dataPlay[3]}')
            return False
        if dataPlay[6] == dataPlay[7] == dataPlay [8]:
            print(f'Победили {dataPlay[6]}')
            return False
        if dataPlay[0] == dataPlay[3] == dataPlay [6]:
            print(f'Победили {dataPlay[0]}')
            return False
        if dataPlay[1] == dataPlay[4] == dataPlay [7]:
            print(f'Победили {dataPlay[1]}')
            return False
        if dataPlay[2] == dataPlay[5] == dataPlay [8]:
            print(f'Победили {dataPlay[2]}')
            return False
        if dataPlay[0] == dataPlay[4] == dataPlay [8]:
            print(f'Победили {dataPlay[0]}')
            return False
        if dataPlay[2] == dataPlay[4] == dataPlay [6]:
            print(f'Победили {dataPlay[2]}')
            return False
        return True

playData = Mygame()

Mygame.playground(playData.playField)
while Mygame.winner(playData.playField):
    for i in range(1,10):
        if i % 2 != 0:
            Mygame.checkPlaygroud(playData.playField, Mygame.playerstep())
            Mygame.playground(playData.playField)
            if Mygame.winner(playData.playField) == False:
                break
        else:
            Mygame.AIstep(playData.playField)
            Mygame.playground(playData.playField)
            if Mygame.winner(playData.playField) == False:
                break
    break               
